import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow

def setQss(file_path, obj):
    with open(file_path, "r") as rf:
        style = rf.read()
        obj.setStyleSheet(style)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setQss("./static/style.qss", app)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())