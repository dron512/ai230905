import sys
from PyQt5.QtWidgets import *

from PyQt5 import uic

form_class = uic.loadUiType("weather.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.table.setColumnCount(4)
        tableColumn = ['지역','최저','최고','날씨']
        self.table.setHorizontalHeaderLabels(tableColumn)
        self.button.clicked.connect(self.btn)

    def btn(self):
        try:
            행개수 = self.table.rowCount()
            self.table.setRowCount(행개수 +1)

            도시 = self.edit1.text() # 현재값 가져오기
            최저 = self.edit2.text()
            최고 = self.edit3.text()
            날씨 = self.edit4.text()

            self.table.setItem(행개수, 0,QTableWidgetItem(도시))
            self.table.setItem(행개수, 1, QTableWidgetItem(최저))
            self.table.setItem(행개수, 2, QTableWidgetItem(최고))
            self.table.setItem(행개수, 3, QTableWidgetItem(날씨))

            self.edit1.setText('') # 빈값으로 만들기
            self.edit2.setText('')
            self.edit3.setText('')
            self.edit4.setText('')
        except Exception as e:
            print(e)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
