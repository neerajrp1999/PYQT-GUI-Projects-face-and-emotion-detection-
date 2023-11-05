from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 593)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/key-6-128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#logoFrame {\n"
"    image: url(:/icon/icon/key-48.ico);\n"
"    border-bottom: 1px solid #fff;\n"
"}\n"
"\n"
"/* Style for menu widget  */\n"
"#menuWidget {\n"
"    background-color: #2B3856;\n"
"}\n"
"\n"
"/* Style for QPushButton in menu widget  */\n"
"#menuWidget QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 15px;\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    font-size: 14px;\n"
"    border: 5px solid #353535;\n"
"    height: 25px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#menuWidget QPushButton:hover {\n"
"    background-color: #e3e3e3;\n"
"}\n"
"\n"
"\n"
"#menuWidget QPushButton:checked {\n"
"    background-color: #0055ff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* Style for main widget */\n"
"#stackedWidget {\n"
"    background-color: #f4f5f8;\n"
"}\n"
"\n"
"/* Style for QLabel in main widget */\n"
"#stackedWidget QLabel {\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"/* Style for QLineEdit and QSpinBox in main widget */\n"
"#stackedWidget QLineEdit, #stackedWidget QSpinBox {\n"
"    border: 1px solid #353535;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button, \n"
"#stackedWidget QSpinBox::up-button {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button:hover, \n"
"#stackedWidget QSpinBox::up-button:hover {\n"
"    background-color: rgb(176, 176, 176);\n"
"}\n"
"\n"
"/* Style for QPushButton in main widget */\n"
"#stackedWidget QPushButton {\n"
"    border: none;\n"
"    font-size: 16px;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"#stackedWidget QPushButton:pressed {\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"/* Style for sepcial QPushButton in main widget */\n"

"#CancelBTN,\n"
"#verifyContactBtn_addnewcontact_page2, \n"
"#showSearchBtn_page3,\n"
"#showSearchBtn_page4,\n"
"#SearchBtn_contact_list_page\n"
"{\n"
"    background-color: #3554d1;\n"
"}\n"
"\n"

"#CancelBTN:hover, #CancelBTN:pressed, \n"
"#verifyContactBtn_addnewcontact_page2:hover,  #verifyContactBtn_addnewcontact_page2:pressed, \n"
"#SearchBtn_contact_list_page:hover,  #SearchBtn_contact_list_page:pressed, \n"
"#showSearchBtn_page4:hover,  #showSearchBtn_page4:pressed, \n"
"#showSearchBtn_page3:hover,  #showSearchBtn_page3:pressed \n"
"{\n"
"    background-color: #0000ff;\n"
"}\n"
"\n"
"#AddContactBtn_addnewcontact_page2, \n"
"#ResetBtn_addnewcontact_page2\n"
"{\n"
"    background-color: #00aa7f;\n"
"}\n"
"\n"
"#AddContactBtn_addnewcontact_page2:hover, #AddContactBtn_addnewcontact_page2:pressed,\n"
"#ResetBtn_addnewcontact_page2:hover, #ResetBtn_addnewcontact_page2:pressed \n"
"{\n"
"    background-color: #00aa00;\n"
"}\n"
"\n"
" #showRefreshBtn_page3,\n"
" #open_file_button_page3,\n"
" #open_file_button_page5,\n"
" #open_file_button_page6,\n"
" #open_file_button_page4,\n"
" #open_file_button_page2,\n"
" #open_file_button_page1\n"
"{\n"
"    background-color: #E59866;\n"
"}\n"
"\n"
"\n"
"#showRefreshBtn_page4:hover, #showRefreshBtn_page4:pressed,\n"
"#open_file_button_page5:hover, #open_file_button_page5:pressed,\n"
"#open_file_button_page6:hover, #open_file_button_page6:pressed,\n"
"#open_file_button_page4:hover, #open_file_button_page4:pressed,\n"
"#showRefreshBtn_page3:hover, #showRefreshBtn_page3:pressed,\n"
"#open_file_button_page3:hover, #open_file_button_page3:pressed,\n"
"#open_file_button_page2:hover, #open_file_button_page2:pressed,\n"
"#open_file_button_page1:hover, #open_file_button_page1:pressed\n"
"{\n"
"    background-color: #DC7633;\n"
"}\n"
"\n"
"/* Style for QFrame */\n"
"#resultFrame {\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.menuWidget = QtWidgets.QWidget(self.centralwidget)
        self.menuWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.menuWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.menuWidget.setObjectName("menuWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        

        self.face_detect_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.face_detect_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.face_detect_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.face_detect_leftmenu_pushButton.setCheckable(False)
        self.face_detect_leftmenu_pushButton.setObjectName("face_detect_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.face_detect_leftmenu_pushButton)

        self.single_image_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.single_image_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.single_image_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.single_image_leftmenu_pushButton.setCheckable(True)
        self.single_image_leftmenu_pushButton.setChecked(True)
        self.single_image_leftmenu_pushButton.setAutoExclusive(True)
        self.single_image_leftmenu_pushButton.setObjectName("single_image_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.single_image_leftmenu_pushButton)
        

        self.multiple_image_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.multiple_image_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.multiple_image_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.multiple_image_leftmenu_pushButton.setCheckable(True)
        self.multiple_image_leftmenu_pushButton.setAutoExclusive(True)
        self.multiple_image_leftmenu_pushButton.setObjectName("multiple_image_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.multiple_image_leftmenu_pushButton)
        
        self.video_clip_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.video_clip_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.video_clip_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.video_clip_leftmenu_pushButton.setCheckable(True)
        self.video_clip_leftmenu_pushButton.setAutoExclusive(True)
        self.video_clip_leftmenu_pushButton.setObjectName("video_clip_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.video_clip_leftmenu_pushButton)

        
        self.web_cam_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.web_cam_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.web_cam_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.web_cam_leftmenu_pushButton.setCheckable(True)
        self.web_cam_leftmenu_pushButton.setAutoExclusive(True)
        self.web_cam_leftmenu_pushButton.setObjectName("web_cam_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.web_cam_leftmenu_pushButton)
        
        self.emotion_detect_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.emotion_detect_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.emotion_detect_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.emotion_detect_leftmenu_pushButton.setCheckable(False)
        self.emotion_detect_leftmenu_pushButton.setObjectName("emotion_detect_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.emotion_detect_leftmenu_pushButton)

        self.image_emotion_detect_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.image_emotion_detect_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.image_emotion_detect_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.image_emotion_detect_leftmenu_pushButton.setCheckable(True)
        self.image_emotion_detect_leftmenu_pushButton.setAutoExclusive(True)
        self.image_emotion_detect_leftmenu_pushButton.setObjectName("image_emotion_detect_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.image_emotion_detect_leftmenu_pushButton)
        

        self.webcam_emotion_detect_leftmenu_pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.webcam_emotion_detect_leftmenu_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.webcam_emotion_detect_leftmenu_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.webcam_emotion_detect_leftmenu_pushButton.setCheckable(True)
        self.webcam_emotion_detect_leftmenu_pushButton.setAutoExclusive(True)
        self.webcam_emotion_detect_leftmenu_pushButton.setObjectName("webcam_emotion_detect_leftmenu_pushButton")
        self.verticalLayout.addWidget(self.webcam_emotion_detect_leftmenu_pushButton)
        


        spacerItem = QtWidgets.QSpacerItem(20, 574, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
       
        self.gridLayout.addWidget(self.menuWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        

        #page1
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.open_file_button_page1 = QtWidgets.QPushButton(self.page)
        self.open_file_button_page1.setMaximumSize(QtCore.QSize(200, 32))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page1.setIcon(icon5)
        self.open_file_button_page1.setObjectName("open_file_button_page1")
        self.gridLayout_3.addWidget(self.open_file_button_page1, 0, 2, 1, 1)
        
        
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        
        self.resultFrame = QtWidgets.QFrame(self.page)
        self.resultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame.setObjectName("resultFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.resultFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label = QtWidgets.QLabel(self.resultFrame)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.resultFrame, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        
        #page2
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_4_page2 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_4_page2.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4_page2.setVerticalSpacing(20)
        self.gridLayout_4_page2.setObjectName("gridLayout_4_page2")
        self.gridLayout_3_page2 = QtWidgets.QGridLayout()
        self.gridLayout_3_page2.setHorizontalSpacing(10)
        self.gridLayout_3_page2.setVerticalSpacing(15)
        self.gridLayout_3_page2.setObjectName("gridLayout_3_page2")

        self.open_file_button_page2 = QtWidgets.QPushButton(self.page2)
        self.open_file_button_page2.setMaximumSize(QtCore.QSize(200, 32))
        icon5_page2 = QtGui.QIcon()
        icon5_page2.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page2.setIcon(icon5_page2)
        self.open_file_button_page2.setObjectName("open_file_button_page2")
        self.gridLayout_3_page2.addWidget(self.open_file_button_page2, 0, 2, 1, 1)
        
        
        self.gridLayout_4_page2.addLayout(self.gridLayout_3_page2, 0, 0, 1, 1)
        
        self.resultFrame_page2 = QtWidgets.QFrame(self.page2)
        self.resultFrame_page2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame_page2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame_page2.setObjectName("resultFrame_page2")
        self.gridLayout_2_page2 = QtWidgets.QGridLayout(self.resultFrame_page2)
        self.gridLayout_2_page2.setObjectName("gridLayout_2_page2")

        self.label_page2 = QtWidgets.QLabel(self.resultFrame_page2)
        self.gridLayout_2_page2.addWidget(self.label_page2, 0, 0, 1, 1)
        self.gridLayout_4_page2.addWidget(self.resultFrame_page2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page2)


        #page3
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_4_page3 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_4_page3.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4_page3.setVerticalSpacing(20)
        self.gridLayout_4_page3.setObjectName("gridLayout_4_page3")
        self.gridLayout_3_page3 = QtWidgets.QGridLayout()
        self.gridLayout_3_page3.setHorizontalSpacing(10)
        self.gridLayout_3_page3.setVerticalSpacing(15)
        self.gridLayout_3_page3.setObjectName("gridLayout_3_page3")

        self.open_file_button_page3 = QtWidgets.QPushButton(self.page3)
        self.open_file_button_page3.setMaximumSize(QtCore.QSize(200, 32))
        icon5_page3 = QtGui.QIcon()
        icon5_page3.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page3.setIcon(icon5_page3)
        self.open_file_button_page3.setObjectName("open_file_button_page3")
        self.gridLayout_3_page3.addWidget(self.open_file_button_page3, 0, 2, 1, 1)
        
        
        self.gridLayout_4_page3.addLayout(self.gridLayout_3_page3, 0, 0, 1, 1)
        
        self.resultFrame_page3 = QtWidgets.QFrame(self.page3)
        self.resultFrame_page3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame_page3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame_page3.setObjectName("resultFrame_page3")
        self.gridLayout_2_page3 = QtWidgets.QGridLayout(self.resultFrame_page3)
        self.gridLayout_2_page3.setObjectName("gridLayout_2_page3")

        self.label_page3 = QtWidgets.QLabel(self.resultFrame_page3)
        self.gridLayout_2_page3.addWidget(self.label_page3, 0, 0, 1, 1)
        self.gridLayout_4_page3.addWidget(self.resultFrame_page3, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page3)




        #page4
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.gridLayout_4_page4 = QtWidgets.QGridLayout(self.page4)
        self.gridLayout_4_page4.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4_page4.setVerticalSpacing(20)
        self.gridLayout_4_page4.setObjectName("gridLayout_4_page4")

        self.gridLayout_3_page4 = QtWidgets.QGridLayout()
        self.gridLayout_3_page4.setHorizontalSpacing(10)
        self.gridLayout_3_page4.setVerticalSpacing(15)
        self.gridLayout_3_page4.setObjectName("gridLayout_3_page4")

        self.open_file_button_page4 = QtWidgets.QPushButton(self.page4)
        self.open_file_button_page4.setMaximumSize(QtCore.QSize(200, 32))
        icon5_page4 = QtGui.QIcon()
        icon5_page4.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page4.setIcon(icon5_page4)
        self.open_file_button_page4.setObjectName("open_file_button_page4")
        self.gridLayout_3_page4.addWidget(self.open_file_button_page4, 0, 2, 1, 1)

        
        
        self.gridLayout_4_page4.addLayout(self.gridLayout_3_page4, 0, 0, 1, 1)

        self.resultFrame_page4 = QtWidgets.QFrame(self.page4)
        self.resultFrame_page4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame_page4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame_page4.setObjectName("resultFrame_page4")
        self.gridLayout_2_page4 = QtWidgets.QGridLayout(self.resultFrame_page4)
        self.gridLayout_2_page4.setObjectName("gridLayout_2_page4")

        self.label_page4 = QtWidgets.QLabel(self.resultFrame_page4)
        self.gridLayout_2_page4.addWidget(self.label_page4, 0, 0, 1, 1)
        self.gridLayout_4_page4.addWidget(self.resultFrame_page4, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page4)
        

        #page5
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.gridLayout_4_page5 = QtWidgets.QGridLayout(self.page5)
        self.gridLayout_4_page5.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4_page5.setVerticalSpacing(20)
        self.gridLayout_4_page5.setObjectName("gridLayout_4_page5")

        self.gridLayout_3_page5 = QtWidgets.QGridLayout()
        self.gridLayout_3_page5.setHorizontalSpacing(10)
        self.gridLayout_3_page5.setVerticalSpacing(15)
        self.gridLayout_3_page5.setObjectName("gridLayout_3_page5")

        self.open_file_button_page5 = QtWidgets.QPushButton(self.page5)
        self.open_file_button_page5.setMaximumSize(QtCore.QSize(200, 32))
        icon5_page5 = QtGui.QIcon()
        icon5_page5.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page5.setIcon(icon5_page5)
        self.open_file_button_page5.setObjectName("open_file_button_page5")
        self.gridLayout_3_page5.addWidget(self.open_file_button_page5, 0, 2, 1, 1)

        
        
        self.gridLayout_4_page5.addLayout(self.gridLayout_3_page5, 0, 0, 1, 1)

        self.resultFrame_page5 = QtWidgets.QFrame(self.page5)
        self.resultFrame_page5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame_page5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame_page5.setObjectName("resultFrame_page5")
        self.gridLayout_2_page5 = QtWidgets.QGridLayout(self.resultFrame_page5)
        self.gridLayout_2_page5.setObjectName("gridLayout_2_page5")

        self.label_page5 = QtWidgets.QLabel(self.resultFrame_page5)
        self.gridLayout_2_page5.addWidget(self.label_page5, 0, 0, 1, 1)
        self.gridLayout_4_page5.addWidget(self.resultFrame_page5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page5)

        #page6
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.gridLayout_4_page6 = QtWidgets.QGridLayout(self.page6)
        self.gridLayout_4_page6.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4_page6.setVerticalSpacing(20)
        self.gridLayout_4_page6.setObjectName("gridLayout_4_page6")

        self.gridLayout_3_page6 = QtWidgets.QGridLayout()
        self.gridLayout_3_page6.setHorizontalSpacing(10)
        self.gridLayout_3_page6.setVerticalSpacing(15)
        self.gridLayout_3_page6.setObjectName("gridLayout_3_page6")

        self.open_file_button_page6 = QtWidgets.QPushButton(self.page6)
        self.open_file_button_page6.setMaximumSize(QtCore.QSize(200, 32))
        icon5_page6 = QtGui.QIcon()
        icon5_page6.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button_page6.setIcon(icon5_page6)
        self.open_file_button_page6.setObjectName("open_file_button_page6")
        self.gridLayout_3_page6.addWidget(self.open_file_button_page6, 0, 2, 1, 1)

        self.gridLayout_4_page6.addLayout(self.gridLayout_3_page6, 0, 0, 1, 1)

        self.resultFrame_page6 = QtWidgets.QFrame(self.page6)
        self.resultFrame_page6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame_page6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame_page6.setObjectName("resultFrame_page6")
        self.gridLayout_2_page6 = QtWidgets.QGridLayout(self.resultFrame_page6)
        self.gridLayout_2_page6.setObjectName("gridLayout_2_page6")

        self.label_page6 = QtWidgets.QLabel(self.resultFrame_page6)
        self.gridLayout_2_page6.addWidget(self.label_page6, 0, 0, 1, 1)
        self.gridLayout_4_page6.addWidget(self.resultFrame_page6, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page6)
        



        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        MainWindow.setVisible(False)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MeetU"))

        self.face_detect_leftmenu_pushButton.setText(_translate("MainWindow", "Face Detect"))
        self.single_image_leftmenu_pushButton.setText(_translate("MainWindow", "1. Single Image"))
        self.multiple_image_leftmenu_pushButton.setText(_translate("MainWindow", "2. Multiple Image"))
        self.video_clip_leftmenu_pushButton.setText(_translate("MainWindow", "3. Video Clip"))
        self.web_cam_leftmenu_pushButton.setText(_translate("MainWindow", "4. Web-Cam"))

        self.emotion_detect_leftmenu_pushButton.setText(_translate("MainWindow", "Emotion Detect"))
        self.image_emotion_detect_leftmenu_pushButton.setText(_translate("MainWindow", "1. Image"))
        self.webcam_emotion_detect_leftmenu_pushButton.setText(_translate("MainWindow", "2. Web-Cam"))

        self.open_file_button_page1.setText(_translate("MainWindow", "Open Image File"))
        self.open_file_button_page2.setText(_translate("MainWindow", "Open Image File"))
        self.open_file_button_page3.setText(_translate("MainWindow", "Open Image File"))
        
        self.open_file_button_page4.setText(_translate("MainWindow", "Open Wb-Cam"))
        self.open_file_button_page5.setText(_translate("MainWindow", "Open Image File"))
        self.open_file_button_page6.setText(_translate("MainWindow", "Open Wb-Cam"))
        
from static import resource_rc