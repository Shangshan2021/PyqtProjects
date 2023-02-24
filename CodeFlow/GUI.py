# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodeFlow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-image: url(:/img/img/BG.jpg);\n"
"}\n"
"")
        self.Menu = QtWidgets.QWidget(Form)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 1280, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu.sizePolicy().hasHeightForWidth())
        self.Menu.setSizePolicy(sizePolicy)
        self.Menu.setMaximumSize(QtCore.QSize(2560, 1800))
        self.Menu.setObjectName("Menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Menu_File = QtWidgets.QPushButton(self.Menu)
        self.Menu_File.setObjectName("Menu_File")
        self.horizontalLayout.addWidget(self.Menu_File)
        self.Menu_Help = QtWidgets.QPushButton(self.Menu)
        self.Menu_Help.setObjectName("Menu_Help")
        self.horizontalLayout.addWidget(self.Menu_Help)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 110, 87, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Menu_File.setText(_translate("Form", "文件"))
        self.Menu_Help.setText(_translate("Form", "帮助"))
        self.label.setText(_translate("Form", "TextLabel"))
import img_rcc_rc
