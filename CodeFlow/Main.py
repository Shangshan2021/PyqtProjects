import sys

from PyQt5.QtWidgets import QApplication

from MainFunc import MyMainWindow


if __name__ == '__main__':
    # init_data()
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())