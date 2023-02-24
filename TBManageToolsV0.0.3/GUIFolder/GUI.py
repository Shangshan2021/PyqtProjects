# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1280, 929)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        MainWidget.setFont(font)
        MainWidget.setStyleSheet("QPushButton{\n"
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
"    }")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_main = QtWidgets.QWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setObjectName("widget_main")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_main)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_leftside = QtWidgets.QWidget(self.widget_main)
        self.widget_leftside.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_leftside.setObjectName("widget_leftside")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_leftside)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_load = QtWidgets.QPushButton(self.widget_leftside)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout_2.addWidget(self.pushButton_load)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_leftside)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_2.addWidget(self.pushButton_save)
        self.widget_API = QtWidgets.QWidget(self.widget_leftside)
        self.widget_API.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_API.setObjectName("widget_API")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_API)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_API)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.textEdit_API = QtWidgets.QTextEdit(self.widget_API)
        self.textEdit_API.setObjectName("textEdit_API")
        self.horizontalLayout_2.addWidget(self.textEdit_API)
        self.verticalLayout_2.addWidget(self.widget_API)
        self.widget_Method = QtWidgets.QWidget(self.widget_leftside)
        self.widget_Method.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_Method.setObjectName("widget_Method")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_Method)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Method = QtWidgets.QLabel(self.widget_Method)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        self.label_Method.setFont(font)
        self.label_Method.setObjectName("label_Method")
        self.horizontalLayout_3.addWidget(self.label_Method)
        self.comboBox_Method = QtWidgets.QComboBox(self.widget_Method)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        self.comboBox_Method.setFont(font)
        self.comboBox_Method.setObjectName("comboBox_Method")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_Method)
        self.verticalLayout_2.addWidget(self.widget_Method)
        self.widget_User = QtWidgets.QWidget(self.widget_leftside)
        self.widget_User.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_User.setObjectName("widget_User")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_User)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_User = QtWidgets.QLabel(self.widget_User)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        self.label_User.setFont(font)
        self.label_User.setObjectName("label_User")
        self.horizontalLayout_4.addWidget(self.label_User)
        self.textEdit_User = QtWidgets.QTextEdit(self.widget_User)
        self.textEdit_User.setObjectName("textEdit_User")
        self.horizontalLayout_4.addWidget(self.textEdit_User)
        self.verticalLayout_2.addWidget(self.widget_User)
        self.label_params = QtWidgets.QLabel(self.widget_leftside)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_params.setFont(font)
        self.label_params.setObjectName("label_params")
        self.verticalLayout_2.addWidget(self.label_params)
        self.textEdit_params = QtWidgets.QTextEdit(self.widget_leftside)
        self.textEdit_params.setMinimumSize(QtCore.QSize(200, 0))
        self.textEdit_params.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.textEdit_params.setFont(font)
        self.textEdit_params.setObjectName("textEdit_params")
        self.verticalLayout_2.addWidget(self.textEdit_params)
        self.label_object = QtWidgets.QLabel(self.widget_leftside)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_object.setFont(font)
        self.label_object.setObjectName("label_object")
        self.verticalLayout_2.addWidget(self.label_object)
        self.textEdit_object = QtWidgets.QTextEdit(self.widget_leftside)
        self.textEdit_object.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.textEdit_object.setFont(font)
        self.textEdit_object.setObjectName("textEdit_object")
        self.verticalLayout_2.addWidget(self.textEdit_object)
        self.label_condition = QtWidgets.QLabel(self.widget_leftside)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_condition.setFont(font)
        self.label_condition.setObjectName("label_condition")
        self.verticalLayout_2.addWidget(self.label_condition)
        self.textEdit_condition = QtWidgets.QTextEdit(self.widget_leftside)
        self.textEdit_condition.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.textEdit_condition.setFont(font)
        self.textEdit_condition.setObjectName("textEdit_condition")
        self.verticalLayout_2.addWidget(self.textEdit_condition)
        self.label_back = QtWidgets.QLabel(self.widget_leftside)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_back.setFont(font)
        self.label_back.setObjectName("label_back")
        self.verticalLayout_2.addWidget(self.label_back)
        self.textEdit_back = QtWidgets.QTextEdit(self.widget_leftside)
        self.textEdit_back.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.textEdit_back.setFont(font)
        self.textEdit_back.setObjectName("textEdit_back")
        self.verticalLayout_2.addWidget(self.textEdit_back)
        self.pushButton_request = QtWidgets.QPushButton(self.widget_leftside)
        self.pushButton_request.setObjectName("pushButton_request")
        self.verticalLayout_2.addWidget(self.pushButton_request)
        self.pushButton_send = QtWidgets.QPushButton(self.widget_leftside)
        self.pushButton_send.setObjectName("pushButton_send")
        self.verticalLayout_2.addWidget(self.pushButton_send)
        self.pushButton_setTask = QtWidgets.QPushButton(self.widget_leftside)
        self.pushButton_setTask.setObjectName("pushButton_setTask")
        self.verticalLayout_2.addWidget(self.pushButton_setTask)
        self.horizontalLayout_6.addWidget(self.widget_leftside)
        self.widget_midside = QtWidgets.QWidget(self.widget_main)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.widget_midside.setFont(font)
        self.widget_midside.setObjectName("widget_midside")
        self.horizontalLayout_6.addWidget(self.widget_midside)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_midside)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qwebengine = QtWebEngineWidgets.QWebEngineView(self.widget_midside)
        self.verticalLayout.addWidget(self.qwebengine)
        self.widget_rightside = QtWidgets.QWidget(self.widget_main)
        self.widget_rightside.setMaximumSize(QtCore.QSize(260, 16777215))
        self.widget_rightside.setObjectName("widget_rightside")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_rightside)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_search = QtWidgets.QTextEdit(self.widget_rightside)
        self.textEdit_search.setMaximumSize(QtCore.QSize(16777215, 20))
        self.textEdit_search.setObjectName("textEdit_search")
        self.verticalLayout.addWidget(self.textEdit_search)
        self.widget_search = QtWidgets.QWidget(self.widget_rightside)
        self.widget_search.setMinimumSize(QtCore.QSize(0, 39))
        self.widget_search.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_search.setObjectName("widget_search")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_search)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_search = QtWidgets.QComboBox(self.widget_search)
        self.comboBox_search.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        self.comboBox_search.setFont(font)
        self.comboBox_search.setObjectName("comboBox_search")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_search)
        self.pushButton_search = QtWidgets.QPushButton(self.widget_search)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        self.verticalLayout.addWidget(self.widget_search)
        self.listView_methods = QtWidgets.QListView(self.widget_rightside)
        self.listView_methods.setObjectName("listView_methods")
        self.verticalLayout.addWidget(self.listView_methods)
        self.horizontalLayout_6.addWidget(self.widget_rightside)
        self.horizontalLayout_5.addWidget(self.widget_main)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "TB TOOL"))
        self.pushButton_load.setText(_translate("MainWidget", "Load"))
        self.pushButton_save.setText(_translate("MainWidget", "Save"))
        self.label.setText(_translate("MainWidget", "API"))
        self.label_Method.setText(_translate("MainWidget", "Method"))
        self.comboBox_Method.setItemText(0, _translate("MainWidget", "GET"))
        self.comboBox_Method.setItemText(1, _translate("MainWidget", "POST"))
        self.comboBox_Method.setItemText(2, _translate("MainWidget", "PUT"))
        self.comboBox_Method.setItemText(3, _translate("MainWidget", "DEL"))
        self.label_User.setText(_translate("MainWidget", "User"))
        self.label_params.setText(_translate("MainWidget", "Params"))
        self.label_object.setText(_translate("MainWidget", "Object"))
        self.textEdit_object.setHtml(_translate("MainWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'仿宋\';\"><br /></p></body></html>"))
        self.label_condition.setText(_translate("MainWidget", "Condition"))
        self.label_back.setText(_translate("MainWidget", "Return"))
        self.pushButton_request.setText(_translate("MainWidget", "Request"))
        self.pushButton_send.setText(_translate("MainWidget", "Send Mail"))
        self.pushButton_setTask.setText(_translate("MainWidget", "Set Auto Tasks"))
        self.textEdit_search.setHtml(_translate("MainWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'华文细黑\'; font-size:10pt;\"><br /></p></body></html>"))
        self.comboBox_search.setItemText(0, _translate("MainWidget", "全部"))
        self.comboBox_search.setItemText(1, _translate("MainWidget", "身份验证(免登)"))
        self.comboBox_search.setItemText(2, _translate("MainWidget", "用户"))
        self.comboBox_search.setItemText(3, _translate("MainWidget", "企业"))
        self.comboBox_search.setItemText(4, _translate("MainWidget", "通讯录"))
        self.comboBox_search.setItemText(5, _translate("MainWidget", "任务"))
        self.comboBox_search.setItemText(6, _translate("MainWidget", "工时"))
        self.comboBox_search.setItemText(7, _translate("MainWidget", "项目"))
        self.comboBox_search.setItemText(8, _translate("MainWidget", "项目分组"))
        self.comboBox_search.setItemText(9, _translate("MainWidget", "角色"))
        self.comboBox_search.setItemText(10, _translate("MainWidget", "名额"))
        self.comboBox_search.setItemText(11, _translate("MainWidget", "群聊"))
        self.comboBox_search.setItemText(12, _translate("MainWidget", "历史版本"))
        self.comboBox_search.setItemText(13, _translate("MainWidget", "其他"))
        self.pushButton_search.setText(_translate("MainWidget", "Search"))