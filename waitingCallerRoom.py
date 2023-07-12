import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, \
    QTableWidgetItem, QPushButton, QHeaderView, \
    QAbstractItemView, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from firebase_admin_tester import *
import main_window

class MainWindowCV(QWidget):
    def __init__(self,user,another_user,another_user_name):
        super(MainWindowCV, self).__init__()
        self.another_user_name=another_user_name
        self.another_user=another_user
        self.user=user
        self.feed=True
        self.VBL = QVBoxLayout()
        self.VBL.setContentsMargins(30, 30, 30, 30)

        self.FeedLabel = QLabel("Calling the "+another_user_name+" , wait for respones..")
        #print(createToken(user))
        self.FeedLabel.setAlignment(Qt.AlignCenter)
        self.VBL.addWidget(self.FeedLabel)

        self.BTN = QPushButton("Drop Call")
        self.BTN.clicked.connect(self.CancelCall)
        self.VBL.addWidget(self.BTN)
        
        #self.Worker1 = Worker1()
        #self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.resize(640,480)
        self.startWork()        

    def CancelCall(self):
        CallDataUpdate(self.another_user,"5")
        #self.setVisibility(False)
        self.hide()
        window = main_window.MainWindow(user_id=self.user)
        window.show()
        

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def startWork(self):
        sendCallRequest(self.user,self.another_user,self.another_user_name)
        #import VideoChatCaller
        #VideoChatCaller.caller(getIpAddress(self.another_user))
        def checkStatus(another_user):
            gotStatus=False
            while not gotStatus:
                status=getStatus(another_user)
                if(status=="1"):
                    continue
                elif(status=="2"):
                    #ringing
                    self.FeedLabel.setText("Ringing the , wait for respones..")
                elif(status=="3"):
                    #call accepted
                    self.close()
                    break
                elif(status=="4"):
                    #ringing
                    self.FeedLabel.setText("Call Decline..")
                    break
        import threading
        callroomThread=threading.Thread(target=checkStatus,args=(self.another_user,))
        callroomThread.start()

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