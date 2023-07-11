# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:15:10 2023

@author: neera
"""
import time
import schedule
from firebase_admin_tester import *
import tkinter as tk
from tkinter import messagebox

UserID=""
canReceiveCall=True
def setUserID(id):
    global UserID
    UserID=id
def BackgroundFunction():
    if(getReceivingCall_Call(UserID)):
        global canReceiveCall
        canReceiveCall=False
        caller=getReceivingCall_CallData(UserID)
        ReceivingCall_CallDataUpdate(UserID,str(2))

        msg_box =  messagebox.askyesno('confirmation', 'Are you sure you want to recieve this call?')
        if msg_box:
            ReceivingCall_CallDataUpdate(UserID,str(3))
            #start calling
        else:
            ReceivingCall_CallDataUpdate(UserID,str(4))
            canReceiveCall=True
            
    print("Geeksforgeeks")
  
schedule.every(20).seconds.do(BackgroundFunction)

def backgroundRunStart():
    while canReceiveCall:
        schedule.run_pending()
        time.sleep(3)
