import sys
from PyQt5.QtWidgets import *

from PyQt5 import uic

import weather_ex
form_class = uic.loadUiType("weather.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.table.setColumnCount(4)
        tableColumn = ['지역','최저','최고','날씨']
        self.table.setHorizontalHeaderLabels(tableColumn)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        # 저장
        self.button.clicked.connect(self.btn)
        # 삭제
        self.button2.clicked.connect(self.btn2)

        try:
            data = weather_ex.doLoad()
            self.table.setRowCount(len(data.index))
            for i in range(len(data.index)):
                for j in range(len(data.columns)):
                    item = QTableWidgetItem(str(data.iloc[i, j]))
                    self.table.setItem(i, j, item)
        except Exception as e:
            print(e)


    def btn(self):
        try:
            행개수 = self.table.rowCount()
            self.table.setRowCount(행개수 +1)

            도시 = self.edit1.text() # 현재값 가져오기
            최저 = self.edit2.text()
            최고 = self.edit3.text()
            날씨 = self.edit4.text()

            weather_ex.doSave(도시,최저,최고,날씨)

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

    def btn2(self):
        try:
            selected_row = self.table.currentRow()
            weather_ex.doDelete(selected_row)
            data = weather_ex.doLoad()
            self.table.setRowCount(len(data.index))
            for i in range(len(data.index)):
                for j in range(len(data.columns)):
                    item = QTableWidgetItem(str(data.iloc[i, j]))
                    self.table.setItem(i, j, item)
        except Exception as e:
            print(e)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
