from os import system
system('cls')

import sys
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)
win = QMainWindow()
textbox = QLineEdit(win)
textout = QLabel("null",win)

    

if __name__ == '__main__':
    textbox.move(100,100)
    textbox.setFixedWidth(200)
    textbox.setPlaceholderText("type something")
    textbox.textChanged.connect(lambda: (textout.setText(textbox.text()), print(textbox.text())))

    textout.move(100,200)
    textout.setFixedWidth(200)

    win.setWindowTitle("Textbox Listener")
    win.setGeometry(100,100,400,400)
    win.show()
    sys.exit(app.exec_())