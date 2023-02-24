# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Schedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Schedule(object):
    def setupUi(self, Schedule):
        Schedule.setObjectName("Schedule")
        Schedule.resize(450, 415)
        Schedule.setStyleSheet("QWidget{\n"
"background-color: rgb(240,208,175) ;\n"
"}\n"
"QPushButton{\n"
"    background-color: gray;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"    border-radius: 14px;\n"
"    padding: 6px;\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QRadioButton{\n"
"font-family: Lucida Bright;\n"
"}\n"
"QLabel{\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QTextEdit{\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QComboBox{\n"
"    background-color: rgb(200,248,245);\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QTimeEdit{\n"
"background-color: rgb(200,248,245);\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"QDateEdit{\n"
"background-color: rgb(200,248,245);\n"
"    font-family: Lucida Bright;\n"
"    }\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Schedule)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_5 = QtWidgets.QWidget(Schedule)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_5)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_select = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_select.setEnabled(True)
        self.comboBox_select.setObjectName("comboBox_select")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_select)
        self.dateEdit = QtWidgets.QDateEdit(self.widget_4)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.timeEdit = QtWidgets.QTimeEdit(self.widget_4)
        self.timeEdit.setTime(QtCore.QTime(17, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_2.addWidget(self.timeEdit)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_radio = QtWidgets.QWidget(self.widget_5)
        self.widget_radio.setEnabled(False)
        self.widget_radio.setObjectName("widget_radio")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_radio)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_radio1 = QtWidgets.QWidget(self.widget_radio)
        self.widget_radio1.setObjectName("widget_radio1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_radio1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_radio1)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_mon = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_mon.setObjectName("radioButton_mon")
        self.horizontalLayout_7.addWidget(self.radioButton_mon)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.widget_radio1)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton_tue = QtWidgets.QRadioButton(self.widget_6)
        self.radioButton_tue.setObjectName("radioButton_tue")
        self.horizontalLayout_8.addWidget(self.radioButton_tue)
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_radio1)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButton_wed = QtWidgets.QRadioButton(self.widget_7)
        self.radioButton_wed.setObjectName("radioButton_wed")
        self.horizontalLayout_9.addWidget(self.radioButton_wed)
        self.horizontalLayout.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.widget_radio1)
        self.widget_radio2 = QtWidgets.QWidget(self.widget_radio)
        self.widget_radio2.setObjectName("widget_radio2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_radio2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.widget_radio2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_thu = QtWidgets.QRadioButton(self.widget)
        self.radioButton_thu.setObjectName("radioButton_thu")
        self.horizontalLayout_5.addWidget(self.radioButton_thu)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_radio2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_fri = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_fri.setObjectName("radioButton_fri")
        self.horizontalLayout_6.addWidget(self.radioButton_fri)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_8 = QtWidgets.QWidget(self.widget_radio2)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButton_workday = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton_workday.setObjectName("radioButton_workday")
        self.horizontalLayout_10.addWidget(self.radioButton_workday)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_radio2)
        self.horizontalLayout_3.addWidget(self.widget_radio)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_apply = QtWidgets.QWidget(Schedule)
        self.widget_apply.setObjectName("widget_apply")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_apply)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_apply)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.widget_apply)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_apply)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_4.addWidget(self.pushButton_apply)
        self.verticalLayout_3.addWidget(self.widget_apply)
        self.widget_note = QtWidgets.QWidget(Schedule)
        self.widget_note.setObjectName("widget_note")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_note)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_note = QtWidgets.QLabel(self.widget_note)
        self.label_note.setObjectName("label_note")
        self.horizontalLayout_11.addWidget(self.label_note)
        self.textEdit_note = QtWidgets.QTextEdit(self.widget_note)
        self.textEdit_note.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textEdit_note.setObjectName("textEdit_note")
        self.horizontalLayout_11.addWidget(self.textEdit_note)
        self.verticalLayout_3.addWidget(self.widget_note)
        self.widget_9 = QtWidgets.QWidget(Schedule)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_token = QtWidgets.QLabel(self.widget_9)
        self.label_token.setObjectName("label_token")
        self.horizontalLayout_12.addWidget(self.label_token)
        self.textEdit_token = QtWidgets.QTextEdit(self.widget_9)
        self.textEdit_token.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_token.setObjectName("textEdit_token")
        self.horizontalLayout_12.addWidget(self.textEdit_token)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(Schedule)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_secret = QtWidgets.QLabel(self.widget_10)
        self.label_secret.setObjectName("label_secret")
        self.horizontalLayout_13.addWidget(self.label_secret)
        self.textEdit_secret = QtWidgets.QTextEdit(self.widget_10)
        self.textEdit_secret.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_secret.setObjectName("textEdit_secret")
        self.horizontalLayout_13.addWidget(self.textEdit_secret)
        self.verticalLayout_3.addWidget(self.widget_10)

        self.retranslateUi(Schedule)
        QtCore.QMetaObject.connectSlotsByName(Schedule)

    def retranslateUi(self, Schedule):
        _translate = QtCore.QCoreApplication.translate
        Schedule.setWindowTitle(_translate("Schedule", "Schedule"))
        self.comboBox_select.setItemText(0, _translate("Schedule", "每日"))
        self.comboBox_select.setItemText(1, _translate("Schedule", "每周"))
        self.comboBox_select.setItemText(2, _translate("Schedule", "每月"))
        self.dateEdit.setDisplayFormat(_translate("Schedule", "d"))
        self.radioButton_mon.setText(_translate("Schedule", "Monday"))
        self.radioButton_tue.setText(_translate("Schedule", "Tuesday"))
        self.radioButton_wed.setText(_translate("Schedule", "Wednesday"))
        self.radioButton_thu.setText(_translate("Schedule", "Thursday"))
        self.radioButton_fri.setText(_translate("Schedule", "Friday"))
        self.radioButton_workday.setText(_translate("Schedule", "Workday"))
        self.label.setText(_translate("Schedule", "Name："))
        self.pushButton_apply.setText(_translate("Schedule", "Apply"))
        self.label_note.setText(_translate("Schedule", "Note:"))
        self.label_token.setText(_translate("Schedule", "dingTalk_token"))
        self.label_secret.setText(_translate("Schedule", "dingTalk_secret"))