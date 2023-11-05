# Import OpenCV library
import cv2
import imutils
def show3(path,label):
    #Load dataset & implemeting xml file

    trainedData=cv2.CascadeClassifier('Face.xml')

    #choose video clip and set position
    webcam=cv2.VideoCapture(path)
    cv2.namedWindow('Video Clip', cv2.WND_PROP_FULLSCREEN)

    while True:
        success,img=webcam.read()
        img = imutils.resize(img, width=950, height=600)

        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #Detect faces
        faceCoordinates=trainedData.detectMultiScale(grayimg)

        for x,y,w,h in faceCoordinates:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        #display image
        cv2.imshow('Video Clip',img)

        #Pause execution until any key pressed
        key = cv2.waitKey(1)
        if(key==81 or key==113):
            break

    webcam.release()