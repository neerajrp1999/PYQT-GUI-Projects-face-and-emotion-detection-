# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:15:10 2023

@author: neera
"""
from stream_ import CameraClient,AudioReceiver,AudioSender,StreamingServer
import threading
import time
import socket
from firebase_admin_tester import *
import tkinter
from tkinter import Label,Button,Tk

class caller:
    def __init__(self,ip_of_send):
        self.window = Tk()
        
        self.panel = Label(self.window,text="wait.. connecting....")
        self.panel.pack(side="top")
        
        self.button = Button(self.window, text='Drop Call', command=self.stop)
        self.button.pack(side="bottom")

        self.window.wm_protocol("WM_DELETE_WINDOW", self.stop)
        self.window.mainloop()
        
        IPAddr = socket.gethostbyname(socket.gethostname())

        self.receiving_audio =AudioReceiver(IPAddr,9007)#your ip
        self.receiving_video =StreamingServer(IPAddr,9006,self.panel)#your ip
        
        self.sending_audio=AudioSender(ip_of_send,9007)
        self.sending_video=CameraClient(ip_of_send,9006)
        
        t1=threading.Thread(target=self.receiving_audio.start_server)
        t1.start()
        t2=threading.Thread(target=self.receiving_video.start_server)
        t2.start()  
        t3=threading.Thread(target=self.sending_audio.start_stream)
        t3.start()
        t4=threading.Thread(target=self.sending_video.start_stream)
        t4.start()
        
    def stop(self):
        self.window.destroy()
        self.sending_video.stop_stream()
        self.sending_audio.stop_stream()
        self.receiving_audio.stop_server()
        self.receiving_video.stop_server()
