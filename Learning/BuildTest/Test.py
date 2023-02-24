# coding = 'utf-8'

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.resize(300, 300)
        self.setWindowTitle('PyQt5')
        self.btn = QPushButton('点击我', self)
        self.btn.resize(100, 30)
        self.lable = QLabel('显示', self)
        self.lable.resize(100, 30)
        self.btn.move(100, 50)
        self.lable.move(100, 100)
        self.btn.clicked.connect(self.clientShow)
        self.show()

    def clientShow(self):
        timeStr = QTime.currentTime().toString('HH:mm:ss')
        self.lable.setText(timeStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())