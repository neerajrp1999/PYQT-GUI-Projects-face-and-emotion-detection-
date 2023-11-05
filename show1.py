# Import OpenCV library
import cv2
import imutils  
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
#Load dataset & implemeting xml file
trainedData=cv2.CascadeClassifier('Face.xml')

def show1(path,label):
    #choose image and set position
    img=cv2.imread(path)
    img=imutils.resize(img, width=100, height=290)

    #convert to gray scale
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect faces
    faceCoordinates=trainedData.detectMultiScale(grayimg)

    # [[131  82 206 206]]
    # print(faceCoordinates)
    x,y,w,h=faceCoordinates[0]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),2)
    
    #display image
    #cv2.imshow('Single Detection',img)
    # cv2.imshow('Single Detection1',img1)
    # using moveWindow() function
    #cv2.moveWindow('Single Detection', 450, 50)
    
    rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgbImage.shape
    bytesPerLine = ch * w
    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
    
    label.setPixmap(QPixmap.fromImage(p))
    #Pause execution until any key pressed
    cv2.destroyAllWindows()
    print('END OF PROGRAM')