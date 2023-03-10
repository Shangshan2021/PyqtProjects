# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Account(object):
    def setupUi(self, Form_Account):
        Form_Account.setObjectName("Form_Account")
        Form_Account.resize(355, 359)
        Form_Account.setStyleSheet("QWidget{\n"
"    background-color: rgb(255,195,195);\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QPushButton{\n"
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
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Account)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_name = QtWidgets.QLabel(Form_Account)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.textEdit_name = QtWidgets.QTextEdit(Form_Account)
        self.textEdit_name.setObjectName("textEdit_name")
        self.verticalLayout.addWidget(self.textEdit_name)
        self.label_account = QtWidgets.QLabel(Form_Account)
        self.label_account.setObjectName("label_account")
        self.verticalLayout.addWidget(self.label_account)
        self.textEdit_account = QtWidgets.QTextEdit(Form_Account)
        self.textEdit_account.setObjectName("textEdit_account")
        self.verticalLayout.addWidget(self.textEdit_account)
        self.radioButton_password = QtWidgets.QRadioButton(Form_Account)
        self.radioButton_password.setObjectName("radioButton_password")
        self.verticalLayout.addWidget(self.radioButton_password)
        self.textEdit_password = QtWidgets.QTextEdit(Form_Account)
        self.textEdit_password.setObjectName("textEdit_password")
        self.verticalLayout.addWidget(self.textEdit_password)
        self.pushButton_confirm = QtWidgets.QPushButton(Form_Account)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.verticalLayout.addWidget(self.pushButton_confirm)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form_Account)
        QtCore.QMetaObject.connectSlotsByName(Form_Account)

    def retranslateUi(self, Form_Account):
        _translate = QtCore.QCoreApplication.translate
        Form_Account.setWindowTitle(_translate("Form_Account", "ConfirmAccount"))
        self.label_name.setText(_translate("Form_Account", "Name"))
        self.label_account.setText(_translate("Form_Account", "Account"))
        self.radioButton_password.setText(_translate("Form_Account", "PassWord"))
        self.pushButton_confirm.setText(_translate("Form_Account", "Confirm"))
