import sys
from PyQt5.QtWidgets import QApplication
from MainFunction import MyMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
