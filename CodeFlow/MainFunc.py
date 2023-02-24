from GUI import Ui_Form
import json
from PyQt5.QtWidgets import QWidget, QFileDialog,QMainWindow


class MyMainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)