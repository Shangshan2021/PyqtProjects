import sys

from PyQt5.QtWidgets import QApplication


from MainFunction import MyMainWindow
from qt_material import apply_stylesheet


if __name__ == '__main__':
    # init_data()
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    MainWindow.show()
    sys.exit(app.exec_())
