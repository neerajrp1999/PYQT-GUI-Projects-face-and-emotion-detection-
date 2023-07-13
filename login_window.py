from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from ui.login_ui import Ui_Form
from main_window import MainWindow
import re
from firebase_admin_tester import *
    
class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.generated_otp=-10
        self.otp_verified=False

        self._startPos = None
        self._endPos = None
        self._tracking = False
    
        self.ui.backBtn_register_page.setFocusPolicy(Qt.NoFocus)
        self.ui.registerBtn_register_page.setFocusPolicy(Qt.NoFocus)
        self.ui.exitBtn_login_page.setFocusPolicy(Qt.NoFocus)
        self.ui.registerBtn_login_page.setFocusPolicy(Qt.NoFocus)
        self.ui.loginBtn_login_page.setFocusPolicy(Qt.NoFocus)
        self.ui.send_otp_Btn_register_page.setFocusPolicy(Qt.NoFocus)
        self.ui.verify_otp_Btn_register_page.setFocusPolicy(Qt.NoFocus)
    
        self.ui.funcWidget.setCurrentIndex(0)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ## login window 
    @pyqtSlot()
    def on_exitBtn_login_page_clicked(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle("Exit?")
        msgBox.setText("Are you sure to EXIT???")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    @pyqtSlot()
    def on_registerBtn_login_page_clicked(self):
        self.ui.funcWidget.setCurrentIndex(1)

    ## register window
    @pyqtSlot()
    def on_backBtn_register_page_clicked(self):
        self.ui.funcWidget.setCurrentIndex(0)

    @pyqtSlot()
    def on_loginBtn_login_page_clicked(self):
        #main_window = MainWindow(user_id="neerajrp1999@gmail.com")
        #main_window.show()
        #self.close()
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()
        if not self.check(username):
            self.warning_messagebox(content="G-Mail ID Is Invalid..")
            return
        if len(password)<3:
            self.warning_messagebox(content="Password lenght must be 4 or more..")
            return
        if(Authenticate(username,password)==0):
            self.warning_messagebox(content="Email Id is not registered in database..")
            return
        elif(Authenticate(username,password)==1):
            self.warning_messagebox(content="Wrong Password..")
            return
        else:
            main_window = MainWindow(user_id=username)
            main_window.show()
            self.close()        
        
    @pyqtSlot()
    def on_verify_otp_Btn_register_page_clicked(self):
        otp = self.ui.otp_lineEdit_register_page.text().strip()
        if len(otp)!=6:
            self.warning_messagebox(content="OTP must be 6 number long ..")
            return
        if int(otp)==self.generated_otp:
            self.otp_verified=True
            self.done_messagebox("OTP Verified...")
        else:
            self.warning_messagebox(content="Wrong OTP...")

    @pyqtSlot()
    def on_send_otp_Btn_register_page_clicked(self):
        gmailid = self.ui.gmail_lineEdit_register_page.text().strip()
        if not self.check(gmailid):
            self.warning_messagebox(content="G-Mail ID Is Invalid..")
            return
        if IsUserAlreadyExist(gmailid):
            self.warning_messagebox(content="User Already Exist..")
            return
        self.sendMail(gmailid)
        self.done_messagebox("OTP is sended to your gmail id..")

    @pyqtSlot()
    def on_registerBtn_register_page_clicked(self):
        gmailid = self.ui.gmail_lineEdit_register_page.text().strip()
        password = self.ui.password_lineEdit_register_page.text().strip()
        name = self.ui.name_lineEdit_register_page.text().strip()
        if not self.check(gmailid):
            self.warning_messagebox(content="G-Mail ID Is Invalid..")
            return
        if IsUserAlreadyExist(gmailid):
            self.warning_messagebox(content="User Already Exist..")
            return
        if len(password)<3:
            self.warning_messagebox(content="Password lenght must be 4 or more..")
            return
        if len(name)<3:
            self.warning_messagebox(content="Name lenght must be 4 or more..")
            return
        if(self.otp_verified):
            InsertNewUser(gmailid,password,name)
            self.done_messagebox("Registation Done...")
            self.ui.gmail_lineEdit_register_page.clear()
            self.ui.otp_lineEdit_register_page.clear()
            self.ui.password_lineEdit_register_page.clear()
            self.ui.funcWidget.setCurrentIndex(0)
        else:
            self.warning_messagebox(content="Verify OTP first...")
        
    def warning_messagebox(self, content):
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
        msgBox.setWindowTitle("Warning")
        msgBox.setText(content)
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.exec_()
        
    def done_messagebox(self, content):
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/verify-50.png"))
        msgBox.setWindowTitle("Info")
        msgBox.setText(content)
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.exec_()
       
    def check(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@gmail.com\b'
        return True if re.fullmatch(regex, email) else False
    
    def sendMail(self,to_mail):
        import smtplib
        import random
        self.generated_otp=random.randint(100000,999999)
        smtplibObject=smtplib.SMTP('smtp.gmail.com',587)
        smtplibObject.ehlo()
        smtplibObject.starttls()
        smtplibObject.login("neerajrp1999.2@gmail.com","qauyldxcqefkjflw")
        message = """
        Subject: Meet U
        
        This message is sended by Meet U Application for creating account.                
        Your OTP is """+str(self.generated_otp)+""" ."""
        smtplibObject.sendmail("neerajrp1999.2@gmail.com",to_mail,message)
        smtplibObject.quit()






