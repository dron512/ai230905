import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import webtoon

form_class = uic.loadUiType("webtoon.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load1.clicked.connect(self.loadEvent)


    def loadEvent(self):
        try:
            titleList = webtoon.doA()
            self.title1.setText(titleList[0])
            self.title2.setText(titleList[1])
            self.title3.setText(titleList[2])
            self.title4.setText(titleList[3])
            self.title5.setText(titleList[4])

            self.img1.setPixmap(QPixmap('img0.png'))
            self.img2.setPixmap(QPixmap('img1.png'))
            self.img3.setPixmap(QPixmap('img2.png'))
            self.img4.setPixmap(QPixmap('img3.png'))
            self.img5.setPixmap(QPixmap('img4.png'))
        except Exception as e:
            print(e)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

