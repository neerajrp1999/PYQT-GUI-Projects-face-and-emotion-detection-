from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.contact_verify=False
        self._is_close=False

        self.single_image_leftmenu_pushButton = self.ui.single_image_leftmenu_pushButton
        self.multiple_image_leftmenu_pushButton = self.ui.multiple_image_leftmenu_pushButton
        self.video_clip_leftmenu_pushButton = self.ui.video_clip_leftmenu_pushButton
        self.web_cam_leftmenu_pushButton = self.ui.web_cam_leftmenu_pushButton
        self.image_emotion_detect_leftmenu_pushButton = self.ui.image_emotion_detect_leftmenu_pushButton
        self.webcam_emotion_detect_leftmenu_pushButton = self.ui.webcam_emotion_detect_leftmenu_pushButton

        self.pages = self.ui.stackedWidget

        self.label=self.ui.label
        self.label_page2=self.ui.label_page2
        self.label_page3=self.ui.label_page3
        self.label_page4=self.ui.label_page4
        self.label_page5=self.ui.label_page5
        self.label_page6=self.ui.label_page6

        self.pages.setCurrentIndex(0)
        
        self.single_image_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.single_image_leftmenu_pushButton))
        self.multiple_image_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.multiple_image_leftmenu_pushButton))
        self.video_clip_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.video_clip_leftmenu_pushButton))
        self.web_cam_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.web_cam_leftmenu_pushButton))
        self.image_emotion_detect_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.image_emotion_detect_leftmenu_pushButton))
        self.webcam_emotion_detect_leftmenu_pushButton.toggled.connect(
            lambda: self.do_change_page(self.webcam_emotion_detect_leftmenu_pushButton))

    # Main window ///////////////////////////////////////////////////////////////
    
    @pyqtSlot()
    def on_open_file_button_page1_clicked(self):
        import  tkinter as tk
        from tkinter import filedialog
        from show1 import show1
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if(file_path):
            show1(file_path,self.label)
    @pyqtSlot()
    def on_open_file_button_page2_clicked(self):
        import  tkinter as tk
        from tkinter import filedialog
        from show2 import show2
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if(file_path):
            show2(file_path,self.label_page2)
    @pyqtSlot()
    def on_open_file_button_page3_clicked(self):
        import  tkinter as tk
        from tkinter import filedialog
        from show3 import show3
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if(file_path):
            show3(file_path,self.label_page2)

    @pyqtSlot(QImage)
    def setImagePage4(self, image):
        self.label_page4.setPixmap(QPixmap.fromImage(image))
    
    @pyqtSlot()
    def on_open_file_button_page4_clicked(self):
        from show4 import Thread,show4
        """
        th = Thread(self)
        if(not self._is_close):
            th.changePixmap.connect(self.setImagePage4)
            th.start()
            self.show()
        else:
            th.release2()
        """
        #or
        show4()
    @pyqtSlot()
    def on_open_file_button_page5_clicked(self):
        import  tkinter as tk
        from tkinter import filedialog
        from show5 import show5
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if(file_path):
            show5(file_path,self.label_page5)
    
    @pyqtSlot(QImage)
    def setImagePage6(self, image):
        self.label_page6.setPixmap(QPixmap.fromImage(image))
    
    @pyqtSlot()
    def on_open_file_button_page6_clicked(self):
        from show6 import Thread,show6
        th = Thread(self)
        if(not self._is_close):
            th.changePixmap.connect(self.setImagePage6)
            th.start()
            self.show()
        else:
            th.release2()
        #or
        #show6()

    def do_change_page(self, btn):
        btn_text = btn.text().strip()
        if btn_text == self.single_image_leftmenu_pushButton.text().strip():
            self.pages.setCurrentIndex(0)
        elif btn_text == self.multiple_image_leftmenu_pushButton.text().strip():
            self.pages.setCurrentIndex(1)
        elif btn_text == self.video_clip_leftmenu_pushButton.text().strip():
            self.pages.setCurrentIndex(2)
        elif btn_text == self.web_cam_leftmenu_pushButton.text().strip():
            self.pages.setCurrentIndex(3)
        elif btn_text == self.image_emotion_detect_leftmenu_pushButton.text().strip():
            self.pages.setCurrentIndex(4)
        else:
            self.pages.setCurrentIndex(5)
