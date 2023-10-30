import sys
from PyQt5.QtWidgets import *
import db

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def insert(self):
        id = self.te1.toPlainText()
        password = self.te2.toPlainText()
        db.doInsert(mid=id, mpass=password)

    def initUI(self):
        label1 = QLabel('Enter your Id')
        self.te1 = QTextEdit()
        label2 = QLabel('Enter your Password')
        self.te2 = QTextEdit()
        btn = QPushButton('저장')
        btn.clicked.connect(self.insert)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(self.te1)
        vbox.addWidget(label2)
        vbox.addWidget(self.te2)
        vbox.addWidget(btn)

        self.setLayout(vbox)

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())