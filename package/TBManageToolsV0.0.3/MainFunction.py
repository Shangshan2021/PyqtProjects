import json
import os

from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel
from tools import trans, statistic, copy_in, getMethodList, data_format
from PyQt5.QtGui import QIcon, QTextCursor
from GUIFolder.GUI import Ui_MainWidget
from GUIFolder.GUI_data import Ui_Form
from GUIFolder.GUI_send import Ui_widget_main
from GUIFolder.GUI_account import Ui_Form_Account
from GUIFolder.GUI_Schedule import Ui_Schedule
from TBFunc import generate
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from SendMail import send_email_attach
import csv


class MyMainWindow(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./Config/Logo.ico'))
        self.pushButton_load.clicked.connect(self.loadParams)
        self.pushButton_request.clicked.connect(self.request)
        self.pushButton_send.clicked.connect(self.send)
        self.pushButton_setTask.clicked.connect(self.setTask)
        self.pushButton_search.clicked.connect(self.search)

        # 实例化列表模型，添加数据
        slm = QStringListModel()
        self.qList = getMethodList()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.qList)
        # 设置列表视图的模型
        self.listView_methods.setModel(slm)
        # 双击触发自定义的槽函数
        self.listView_methods.doubleClicked.connect(self.select)

        self.pushButton_save.clicked.connect(self.saveParams)
        self.qwebengine.load(QtCore.QUrl('https://open.teambition.com/docs/documents/5d89a927a55fbd000120c30c'))

    def loadParams(self):
        try:
            dialog = QFileDialog()
            filepath, type = dialog.getOpenFileName(self, "选择配置文件", "./Config/ParamsFile/ConfigFile",
                                                    'json(*.json)')
            if type:
                config = open(filepath, encoding='utf-8', mode='r')
                data = json.load(config)
                self.textEdit_API.setText(data['url'])
                self.textEdit_User.setText(data['user'])
                self.comboBox_Method.setCurrentText(data['method'])
                self.textEdit_params.setText(data['params'])
                self.textEdit_object.setText(data['object'])
                self.textEdit_condition.setText(data['condition'])
                self.textEdit_back.setText(data['back'])
            else:
                QMessageBox.information(self, "Error Message", 'File cannot be empty!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def saveParams(self):
        try:
            data = {
                'url': self.textEdit_API.toPlainText(),
                'method': self.comboBox_Method.currentText(),
                'user': self.textEdit_User.toPlainText(),
                'params': self.textEdit_params.toPlainText(),
                'object': self.textEdit_object.toPlainText(),
                'condition': self.textEdit_condition.toPlainText(),
                'back': self.textEdit_back.toPlainText()
            }
            dialog = QFileDialog()
            filepath, type = dialog.getSaveFileName(self, "配置文件保存", "./Config/ParamsFile/ConfigFile",
                                                    'json(*.json)')
            if type:
                config = open(filepath, encoding="utf-8", mode='w')
                json.dump(data, config)
                config.close()
            else:
                QMessageBox.information(self, "Error Message", 'File cannot be empty!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def request(self):
        try:
            api = self.textEdit_API.toPlainText()
            method = self.comboBox_Method.currentText()
            user = self.textEdit_User.toPlainText()
            params = trans(self.textEdit_params.toPlainText().split('\n'))
            object = trans(self.textEdit_object.toPlainText().split('\n'))
            conditions = self.textEdit_condition.toPlainText().split('\n')
            backs = self.textEdit_back.toPlainText().split('\n')
            config_data={'api':api,'method':method,'user':user,'params':params,'object':object,'conditions':conditions,'backs':backs}
            data,nextPageToken ,count= generate(api, method, user, params, object, conditions, backs)
            self.gui_data = WidgetData(data, config_data,nextPageToken,count)
            self.gui_data.show_widget()
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def send(self):
        try:
            self.gui_send = WidgetSend()
            self.gui_send.show_widget()
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def setTask(self):
        try:
            data = {
                'url': self.textEdit_API.toPlainText(),
                'method': self.comboBox_Method.currentText(),
                'user': self.textEdit_User.toPlainText(),
                'params': self.textEdit_params.toPlainText(),
                'object': self.textEdit_object.toPlainText(),
                'condition': self.textEdit_condition.toPlainText(),
                'back': self.textEdit_back.toPlainText()
            }
            self.gui_send = WidgetSchedule(data)
            self.gui_send.show_widget()
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def search(self):
        try:
            kind = self.comboBox_search.currentText()
            text = self.textEdit_search.toPlainText()
            file = open('./Config/Methods.json', encoding='utf-8', mode='r')
            methods = list(json.load(file).keys())
            methods_filter = [_ for _ in methods if _.split('_')[0] == kind]
            if text != '' and text:
                methods_filter = [_ for _ in methods_filter if _.find(text) != -1]
            slm = QStringListModel()
            self.qList = methods_filter
            slm.setStringList(self.qList)
            # 设置列表视图的模型
            self.listView_methods.setModel(slm)

        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def select(self, qModelIndex):
        """
        __TODO__:
        添加 ·参数· 字段
        保存常用的参数，例如：
        项目id
        自定义参数id
        人员id

        :param qModelIndex:
        :return:
        """

        try:
            methods = json.load(open('./Config/Methods.json', encoding='utf-8', mode='r'))
            name = self.qList[qModelIndex.row()]
            url = methods[name]
            self.qwebengine.load(QtCore.QUrl(url))
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)


class WidgetData(QWidget, Ui_Form):
    def __init__(self, data, config_data,nextPageToken,count):
        super(WidgetData, self).__init__()
        self.setupUi(self)
        self.page_count=50
        self.count=count
        self.config_data=config_data
        self.data = data_format(data)
        self.backs = config_data['backs']
        self.nextPageToken=nextPageToken
        self.setWindowIcon(QIcon('./Config/Logo.ico'))
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_copy.clicked.connect(self.copy)
        if nextPageToken is not None:
            self.pushButton_next.setEnabled(True)
        self.pushButton_next.clicked.connect(self.next)

    def show_widget(self):
        self.show()
        self.load_data(self.data, self.backs)

    def load_data(self, data, backs):
        self.textEdit_data.textCursor().insertText("相关查询结果如下：\n")
        self.textEdit_data.textCursor().movePosition(QTextCursor.End)
        """
        __TODO__:
        这里需要处理一下数据
        现在的数据还是太丑了
        """
        self.label_count.setText(f'{self.page_count}/{self.count}')
        _table = self.textEdit_data.textCursor().insertTable(len(data) + 1, len(backs))
        statistic(_table, backs, data)

    def next(self):
        try:
            cd=self.config_data
            data, self.nextPageToken,self.count= generate(cd['api'], cd['method'], cd['user'], cd['params'], cd['object'], cd['conditions'], cd['backs'],self.nextPageToken)
            self.page_count+=50
            if self.page_count-self.count>=50:
                self.page_count=50
            self.textEdit_data.clear()
            self.load_data(data,self.backs)

        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def save(self):
        try:
            dialog = QFileDialog()
            filepath, type = dialog.getSaveFileName(self, "数据文件保存", "./Data",
                                                    'csv(*.csv)')
            if type:
                with open(filepath, encoding='utf-8', mode='w+', newline="") as csv_file:
                    csv_write = csv.DictWriter(csv_file, self.backs)
                    csv_write.writeheader()
                    for _ in self.data:
                        csv_write.writerow(_)
                """
                __TODO__:
                这里要处理数据后写入csv文件
                """
                QMessageBox.information(self, "Note Message", 'File Saved Successfully!', QMessageBox.Yes)
            else:
                QMessageBox.information(self, "Error Message", 'File cannot be empty!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def copy(self):
        try:
            copy_in(str(self.data))
            QMessageBox.information(self, "Note Message", 'Copy Successfully!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)


class WidgetSend(QWidget, Ui_widget_main):
    def __init__(self):
        super(WidgetSend, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./Config/Logo.ico'))
        self.pushButton_attach.clicked.connect(self.attach)
        self.pushButton_sender.clicked.connect(self.sender)
        self.pushButton_filedata.clicked.connect(self.filedata)
        self.pushButton_recipient.clicked.connect(self.recipient)
        self.init_combox()
        self.csv = []

    def show_widget(self):
        self.show()

    def init_combox(self):
        recipients_js = open('./Config/recipients.json', encoding='utf-8', mode='r+')
        data = json.load(recipients_js)
        self.comboBox_recipient.clear()
        for name in data.keys():
            self.comboBox_recipient.addItem(name)
        senders_js = open('./Config/senders.json', encoding='utf-8', mode='r+')
        data = json.load(senders_js)
        self.comboBox_sender.clear()
        for name in data.keys():
            self.comboBox_sender.addItem(name)

    def attach(self):
        try:
            dialog = QFileDialog()
            filepath, type = dialog.getOpenFileName(self, "选择数据文件", "./Data",
                                                    'csv(*.csv)')
            if type:
                self.csv.append(filepath)
            else:
                QMessageBox.information(self, "Error Message", 'File cannot be empty!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def sender(self):
        try:
            if self.comboBox_sender.currentText() == 'Add New Sender':
                self.gui_senderAccount = WidgetAccount()
                self.gui_senderAccount.show_widget()
                self.gui_senderAccount.require()
                self.init_combox()
            else:
                senders_js = open('./Config/senders.json', encoding='utf-8', mode='r+')
                data = json.load(senders_js)
                if send_email_attach(self.textEdit_send.toPlainText().split('\n'),
                                     data[self.comboBox_sender.currentText()][0],
                                     data[self.comboBox_sender.currentText()][1], self.textEdit_content.toPlainText(),
                                     self.csv):
                    QMessageBox.information(self, "Note Message.", 'Sent Successfully.', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def filedata(self):
        try:
            pass
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)

    def recipient(self):
        try:
            if self.comboBox_recipient.currentText() == 'Add New Recipient':
                self.gui_recipientAccount = WidgetAccount()
                self.gui_recipientAccount.show_widget()
                self.init_combox()
            else:
                file = open('./Config/recipients.json', encoding='utf-8', mode='r+')
                recipients = json.load(file)
                if recipients[self.comboBox_recipient.currentText()] in self.textEdit_send.toPlainText():
                    QMessageBox.information(self, "Note Message", 'Address already exists.', QMessageBox.Yes)
                else:
                    if self.textEdit_send.toPlainText() == '':
                        self.textEdit_send.setText(f'{recipients[self.comboBox_recipient.currentText()]}')
                    else:
                        self.textEdit_send.append(f'{recipients[self.comboBox_recipient.currentText()]}')
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)


class WidgetAccount(QWidget, Ui_Form_Account):
    def __init__(self):
        super(WidgetAccount, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./Config/Logo.ico'))
        self.pushButton_confirm.clicked.connect(self.confirm)

    def require(self):
        self.radioButton_password.setChecked(True)

    def show_widget(self):
        self.show()

    def confirm(self):
        try:
            print(self.radioButton_password.isChecked())
            if self.radioButton_password.isChecked():
                file = open('./Config/senders.json', encoding='utf-8', mode='w+')
                senders = json.load(file)
                names = self.textEdit_name.toPlainText().split('\n')
                accounts = self.textEdit_account.toPlainText().split('\n')
                passwords = self.textEdit_password.toPlainText().split('\n')
                for i in range(0, len(names)):
                    senders[names[i]] = [accounts[i], passwords[i]]
                json.dump(senders, file)
                file = open('./Config/recipients.json', encoding='utf-8', mode='w+')
                recipients = json.load(file)
                recipients[self.textEdit_name.toPlainText()] = self.textEdit_account.toPlainText()
                json.dump(recipients, file)
            else:
                file = open('./Config/recipients.json', encoding='utf-8', mode='r+')
                recipients = json.load(file)
                names = self.textEdit_name.toPlainText().split('\n')
                accounts = self.textEdit_account.toPlainText().split('\n')
                for i in range(0, len(names)):
                    recipients[names[i]] = accounts[i]
                file = open('./Config/recipients.json', encoding='utf-8', mode='w+')
                json.dump(recipients, file)
            QMessageBox.information(self, "Note Message", 'Added Successfully.', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)


class WidgetSchedule(QWidget, Ui_Schedule):
    def __init__(self,data):
        super(WidgetSchedule, self).__init__()
        self.setupUi(self)
        self.data=data
        self.setWindowIcon(QIcon('./Config/Logo.ico'))
        self.comboBox_select.currentIndexChanged.connect(self.Period_select)
        self.radioButton_workday.clicked.connect(self.workday)
        self.pushButton_apply.clicked.connect(self.apply_schedule)

    def show_widget(self):
        self.show()

    def Period_select(self):
        if self.comboBox_select.currentText() == '每月':
            self.dateEdit.setEnabled(True)
            self.widget_radio.setEnabled(False)
        elif self.comboBox_select.currentText() == '每日':
            self.dateEdit.setEnabled(False)
            self.widget_radio.setEnabled(False)
        elif self.comboBox_select.currentText() == '每周':
            self.dateEdit.setEnabled(False)
            self.widget_radio.setEnabled(True)

    def workday(self):
        if self.radioButton_workday.isChecked():
            self.radioButton_fri.setChecked(False)
            self.radioButton_mon.setChecked(False)
            self.radioButton_thu.setChecked(False)
            self.radioButton_tue.setChecked(False)
            self.radioButton_wed.setChecked(False)
            self.widget_radio1.setEnabled(False)
            self.radioButton_fri.setEnabled(False)
            self.radioButton_thu.setEnabled(False)
        else:
            self.widget_radio1.setEnabled(True)
            self.radioButton_fri.setEnabled(True)
            self.radioButton_thu.setEnabled(True)

    def apply_schedule(self):
        try:
            if self.textEdit.toPlainText() == '':
                taskname = 'DefaultName'
            else:
                taskname = self.textEdit.toPlainText()
            if self.comboBox_select.currentText() == '每周':
                weektime = ''
                if self.radioButton_workday.isChecked():
                    weektime = 'MON,TUE,WED,THU,FRI'
                else:
                    if self.radioButton_tue.isChecked():
                        weektime += 'TUE'
                    if self.radioButton_mon.isChecked():
                        if weektime != '':
                            weektime += ','
                        weektime += 'MON'
                    if self.radioButton_wed.isChecked():
                        if weektime != '':
                            weektime += ','
                        weektime += 'WED'
                    if self.radioButton_thu.isChecked():
                        if weektime != '':
                            weektime += ','
                        weektime += 'THU'
                    if self.radioButton_fri.isChecked():
                        if weektime != '':
                            weektime += ','
                        weektime += 'FRI'
                taskroll = f'weekly /d {weektime}'
            elif self.comboBox_select.currentText() == '每日':
                taskroll = 'daily'
            else:
                taskroll = f'monthly /d {self.dateEdit.date().day()}'

            self.data['dingTalk_token']=self.textEdit_token.toPlainText()
            self.data['dingTalk_secret']=self.textEdit_secret.toPlainText()
            self.data['Note']=self.textEdit_note.toPlainText()
            dialog = QFileDialog()
            filepath, type = dialog.getSaveFileName(self, "配置文件保存", "./Config/ParamsFile/ConfigFile",
                                                    'json(*.json)')
            if type:
                config = open(filepath, encoding="utf-8", mode='w')
                json.dump(self.data, config)
                config.close()
            else:
                QMessageBox.information(self, "Error Message", 'File cannot be empty!', QMessageBox.Yes)

            f=open(f'./AutoTask/{taskname}.bat')
            f.write(f'Post_Ding.exe --{filepath}')

            folder_path = os.path.dirname(os.path.abspath(__file__))
            file_path = folder_path + f"\\AutoTask\\{taskname}.bat"

            cmd = f'schtasks /create /tn {str(taskname)} /tr {str(file_path)} /sc {str(taskroll)} /st {str(self.timeEdit.time().toPyTime())}'
            os.popen(cmd)
            QMessageBox.information(self, "Note Message", 'Auto Task Set Successfully!', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Error Message", str(e), QMessageBox.Yes)
