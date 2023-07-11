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

class caller:
    def __init__(self,ip_of_send):
        self.sending_audio=AudioSender(ip_of_send,9997)
        self.sending_video=CameraClient(ip_of_send,9996)

        t3=threading.Thread(target=self.sending_audio.start_stream)
        t3.start()
        time.sleep(2)
        t4=threading.Thread(target=self.sending_video.start_stream)
        t4.start()

        IPAddr = socket.gethostbyname(socket.gethostname())

        self.receiving_audio =AudioReceiver(IPAddr,9997)#your ip
        self.receiving_video =StreamingServer(IPAddr,9996)#your ip

        t1=threading.Thread(target=self.receiving_audio.start_server)
        t1.start()
        time.sleep(2)
        t2=threading.Thread(target=self.receiving_video.start_server)
        t2.start()

    def stop(self):
        self.sending_video.stop_stream()
        self.sending_audio.stop_stream()
        self.receiving_audio.stop_stream()
        self.receiving_video.stop_stream()

"""
def caller(ip_of_send):
    sending_audio=AudioSender(ip_of_send,9997)
    sending_video=CameraClient(ip_of_send,9996)

    t3=threading.Thread(target=sending_audio.start_stream)
    t3.start()
    time.sleep(2)
    t4=threading.Thread(target=sending_video.start_stream)
    t4.start()

    IPAddr = socket.gethostbyname(socket.gethostname())

    receiving_audio =AudioReceiver(IPAddr,9997)#your ip
    receiving_video =StreamingServer(IPAddr,9996)#your ip

    t1=threading.Thread(target=receiving_audio.start_server)
    t1.start()
    time.sleep(2)
    t2=threading.Thread(target=receiving_video.start_server)
    t2.start()
    t3=threading.Thread(target=sc)
    t3.start()

    while input("")!= "STOP":
        continue

    sending_video.stop_stream()
    sending_audio.stop_stream()
"""