import cv2
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage



class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    def release2(self):
        if(self.cap.isOpened()):
            self.cap.release()
    def run(self):
        self.trainedData=cv2.CascadeClassifier('Face.xml')
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, frame = self.cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faceCoordinates=self.trainedData.detectMultiScale(grayimg)

                for x,y,w,h in faceCoordinates:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                key = cv2.waitKey(1)
                
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
def show4():
    import imutils
    trainedData=cv2.CascadeClassifier('Face.xml')
    webcam=cv2.VideoCapture(0)
    while True:
        success,img=webcam.read()
        img = imutils.resize(img, width=850, height=500)

        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faceCoordinates=trainedData.detectMultiScale(grayimg)

        for x,y,w,h in faceCoordinates:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow('Face Detect',img)
        cv2.moveWindow('Face Detect', 450, 50)

        key = cv2.waitKey(1)

        if(key==81 or key==113):
            break

    webcam.release()