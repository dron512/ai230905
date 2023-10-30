import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import loadnews

form_class = uic.loadUiType("news.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load_btn.clicked.connect(self.load)

    def load(self):
        src,text = loadnews.doload()
        print(src,text)
        map = QPixmap(src)
        map = map.scaled(850, 270)
        self.label.setPixmap(map)
        self.label_2.setText(text)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
