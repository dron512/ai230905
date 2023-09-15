import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import ex02

form_class = uic.loadUiType("friend.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.savebtn.clicked.connect(self.saveEvent)
        self.loadbtn.clicked.connect(self.loadEvent)
    def saveEvent(self):
        print('save')
    def loadEvent(self):
        result = ex02.doLoad()
        self.textid.setText(result)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
