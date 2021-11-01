import sys

from os import system
system('cls')

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets as qt

class LoginForm:
    def __init__(self, win, uname, pasw):
        # validation strings
        self.username = uname
        self.password = pasw

        # username object
        self.lbl_name = qt.QLabel("Login Field", win)
        self.lbl_name.move(50,50)
        self.txf_name = qt.QLineEdit(win)
        self.txf_name.move(50,80)
        self.txf_name.setFixedWidth(200)

        # password object
        self.lbl_pasw = qt.QLabel("Password Field", win)
        self.lbl_pasw.move(self.txf_name.width() + 100,50)
        self.txf_pasw = qt.QLineEdit(win)
        self.txf_pasw.move(self.txf_name.width() + 100,80)
        self.txf_pasw.setFixedWidth(200)

        # output object
        self.lbl_outp = qt.QLabel("Hi", win)
        self.lbl_outp.setFont(QFont("Segoe UI",14))
        self.lbl_outp.move(50,150)
        self.lbl_outp.setFixedWidth(200)
        self.lbl_outp.setStyleSheet("border: 1px solid black;")

        # login object
        self.btn_run = qt.QPushButton("Login",win)
        self.btn_run.move(self.txf_pasw.x() + self.txf_pasw.width() + 50,80)
        self.btn_run.clicked.connect(self.func_login)
        
    def func_login(self):
        isNameValid = self.txf_name.text().lower() == self.username.lower()
        isPaswValid = self.txf_pasw.text().lower() == self.password.lower()
        if (isNameValid and isPaswValid):
            print("Login Successful")
            self.lbl_outp.setText("Login Successful")
            self.lbl_outp.setStyleSheet("color: green; font-weight: bold")
        else:
            print("Login Failed")
            self.lbl_outp.setText("Login Failed")
            self.lbl_outp.setStyleSheet("color: red; font-weight: bold")
        
        
def main():
    app = qt.QApplication(sys.argv)
    win = qt.QMainWindow()

    struct_login = LoginForm(win, "Joeninyo", "isAwesome")

    xpos = 200; ypos = 200; width = 700; height = 250

    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Login Window")
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print(__name__, "session started")
    main()