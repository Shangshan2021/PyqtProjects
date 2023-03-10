# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Generate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 802)
        Form.setStyleSheet("QPushButton{\n"
"    background-color: gray;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"    border-radius: 14px;\n"
"    padding: 6px;\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QWidget#MainWidget{\n"
"    background-color: rgb(240,248,255);\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QLabel{\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QTextEdit{\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QComboBox{\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QWidget#widget_main{\n"
"    background-color: rgb(32,178,170);\n"
"    font-family: Lucida Bright;\n"
"    }")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_main = QtWidgets.QWidget(Form)
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_data = QtWidgets.QTextEdit(self.widget_main)
        self.textEdit_data.setObjectName("textEdit_data")
        self.verticalLayout.addWidget(self.textEdit_data)
        self.widget_bt = QtWidgets.QWidget(self.widget_main)
        self.widget_bt.setObjectName("widget_bt")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_bt)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_next = QtWidgets.QPushButton(self.widget_bt)
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.label_count = QtWidgets.QLabel(self.widget_bt)
        self.label_count.setObjectName("label_count")
        self.horizontalLayout.addWidget(self.label_count)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_copy = QtWidgets.QPushButton(self.widget_bt)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.horizontalLayout.addWidget(self.pushButton_copy)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_bt)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout.addWidget(self.widget_bt)
        self.verticalLayout_2.addWidget(self.widget_main)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_next.setText(_translate("Form", "Next Page"))
        self.label_count.setText(_translate("Form", "Page/Count"))
        self.pushButton_copy.setText(_translate("Form", "Copy"))
        self.pushButton_save.setText(_translate("Form", "Save"))
