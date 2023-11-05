# Import OpenCV library
import cv2 
import imutils
# Import OpenCV library
import cv2
import imutils  
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

def show2(path,label):
    #Load dataset & implemeting xml file
    trainedData=cv2.CascadeClassifier('Face.xml')

    #choose image and position
    img=cv2.imread(path)
    img = imutils.resize(img, width=980, height=500)

    #convert to gray scale
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect faces
    faceCoordinates=trainedData.detectMultiScale(grayimg)
    # [[446 145 149 149]
    #  [397 296 131 131]
    #  [249 194 138 138]
    #  [287 431 134 134]
    #  [677 257 222 222]
    #  [136 403 154 154]]
    # print(faceCoordinates)

    # x,y,w,h=faceCoordinates[0]
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),2)
    # x,y,w,h=faceCoordinates[1]
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),2)
    for x,y,w,h in faceCoordinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),2)

    #display image
    #cv2.imshow('Multiple Detection',img)
    #cv2.moveWindow('Multiple Detection', 350, 50)

    #Pause execution until any key pressed
    rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgbImage.shape
    bytesPerLine = ch * w
    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
    
    label.setPixmap(QPixmap.fromImage(p))
    #Pause execution until any key pressed
    cv2.destroyAllWindows()
    print('END OF PROGRAM')

    print('END OF PROGRAM')