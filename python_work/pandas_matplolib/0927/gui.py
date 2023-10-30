#https://wikidocs.net/35482
import sys
from PyQt5.QtWidgets import *

from PyQt5 import uic

import luck

form_class = uic.loadUiType("luck.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.load_today.clicked.connect(self.today)
        self.load_year.clicked.connect(self.year)

    def today(self):
        self.result.setText(luck.doToday())
    def year(self):
        self.result.setText(luck.doYear())


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
