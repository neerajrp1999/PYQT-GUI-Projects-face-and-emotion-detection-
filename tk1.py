import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, \
    QTableWidgetItem, QPushButton, QHeaderView, \
    QAbstractItemView, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from firebase_admin_tester import *
import VideoChatCaller
from tkinter import *       
class caller():
    def __init__(self,user,another_user,another_user_name):
        self.another_user_name=another_user_name
        self.another_user=another_user
        self.user=user
        self.feed=True
        self.root = Tk()
        self.root.geometry('640x480')
        self.FeedLabel=Label(self.root,text="Calling....   wait for response....")
        self.FeedLabel.place(x=225, y=50) 
        btn = Button(self.root, text = 'Drop Call', command = lambda:self.CancelCall())
        btn.place(x=270, y=300) 
        self.startWork()        
        self.root.mainloop()
    
    def CancelCall(self):
        CallDataUpdate(self.another_user,"5")
        self.root.destroy()
        #self.hide()
        #window = main_window.MainWindow(user_id=self.user)
        #window.show()
        

    def ImageUpdateSlot(self, Image):
        #self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        pass

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
                    #self.close()
                    self.root.destroy()
                    VideoChatCaller.caller()

                    break
                elif(status=="4"):
                    #ringing
                    self.FeedLabel.setText("Call Decline..")
                    break
        import threading
        callroomThread=threading.Thread(target=checkStatus,args=(self.another_user,))
        callroomThread.start()

if __name__=="__main__":
    caller()