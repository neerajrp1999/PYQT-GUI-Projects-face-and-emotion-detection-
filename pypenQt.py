import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

class MainWindowCV(QWidget):
    def __init__(self):
        super(MainWindowCV, self).__init__()
        
        self.feed=True
        self.VBL = QVBoxLayout()
        self.VBL.setContentsMargins(30, 30, 30, 30)

        self.FeedLabel = QLabel("Call ?")
        self.FeedLabel.setAlignment(Qt.AlignCenter)
        self.VBL.addWidget(self.FeedLabel)

        self.BTN = QPushButton("Start")
        self.BTN.clicked.connect(self.Feed)
        self.VBL.addWidget(self.BTN)
        
        #self.startBTN = QPushButton("start")
        #self.startBTN.clicked.connect(self.startFeed)
        #self.VBL.addWidget(self.startBTN)

        self.Worker1 = Worker1()
        
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.resize(640,480)
        #self.Feed()        

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def Feed(self):
        if(self.feed):
            self.Worker1.start()
            self.feed=False
            self.BTN.setText("Cancel")
        else:
            self.Worker1.stop()
            self.close()

        

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
        Capture.release()
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindowCV()
    Root.show()
    sys.exit(App.exec())