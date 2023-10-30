import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import loadWeather

form_class = uic.loadUiType("weather.ui")[0]

cnt = 0
imglist = ['a.png','b.png','c.png']

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.load_btn.clicked.connect(self.loadEvent)
        self.gra_btn.clicked.connect(self.imageEvent)


    def loadEvent(self):
        try:
            result = loadWeather.doload()
            self.result_label.setText(result.split("\n")[1])
            self.result_label_2.setText(result.split("\n")[0])
        except Exception as e:
            print(e)
        '''
            문제 1
            현재는 a.png 라는 이미지만 생성되어져 있습니다.
            b.png와 c.png 이미지를 생성하고
                gra_btn 버튼을 눌렀을시에 
                a.png
                b.png
                c.png 를 순서대로 나올수 있도록 해주세요
            문제 2
            urlretrieve 함수를 사용하여 웹에서 이미지 파일을
            다운로드 하는 방법을 찾아서 해보도록 합니다.
        '''

    def imageEvent(self):
        # import matplotlib.pyplot as plt
        #
        # plt.plot([10,20], [30,40])
        # plt.savefig('a.png')
        global cnt
        map = QPixmap(imglist[cnt%3])
        map = map.scaled(850,270)
        self.myImage_label.setPixmap(map)
        cnt += 1

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
