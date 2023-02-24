import sys

import requests
from function import md2html
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from connect import Ui_Form
from Qt_config import init_qt,init_data,checkin_data
import connect
from PyQt5 import uic


class MyMainWindow(QWidget,Ui_Form ):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Init_Button.clicked.connect(init_data)
        self.options_init(init_qt())
        self.Start_Button.clicked.connect(self.start)
        self.Add_Button.clicked.connect(self.add_parameter)
        self.exit_Button.clicked.connect(self.exit)
        self.GeneralInfo()

    def exit(self):
        sys.exit()

    def GeneralInfo(self):
        md=open('TQL.md',encoding='utf-8',mode='r+')
        self.Info.setMarkdown(md.read())

    def options_init(self,data):
             for name in data['API'][0].keys():
                self.API_comboBox.addItem(name)
             for name in data['User'][0].keys():
                self.User_comboBox.addItem(name)
             for name in data['method'][0].keys():
                self.Method_comboBox.addItem(name)

    def start(self):

        message=self.Parameter_box.currentText()
        QMessageBox.information(self, "信息提示框", message)

    def add_parameter(self):
        name=str(self.Parameter_box.currentText())
        value=self.value_edit.toPlainText()
        Parameter=self.Parameter_edit.toPlainText()
        if name=='API':
            self.API_comboBox.addItem(Parameter)
        elif name=='User':
            self.User_comboBox.addItem(Parameter)
        data=init_qt()
        data[name][0][Parameter]=value
        print(data)
        checkin_data(data)


if __name__ == '__main__':
    # init_data()
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

