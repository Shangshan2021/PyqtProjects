import csv
import os
import shutil

from PyQt5.QtGui import QTextCursor, QIcon

from GUI import Ui_MainWidget
import json
from PyQt5.QtWidgets import QWidget, QFileDialog
from functions import search_data, trans, generate, statistic
from Send_File import send_email_attach


class MyMainWindow(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('Logo.ico'))
        self.gui_init()
        self.pushButton_exit.clicked.connect(self.exit_clear)
        # self.pushButton_addparameter.clicked.connect(self.addparameter)
        self.pushButton_ensure.clicked.connect(self.ensure)
        self.pushButton_update.clicked.connect(self.updatetext)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_del.clicked.connect(self.dele)
        self.pushButton_send.clicked.connect(self.send)
        self.pushButton_data.clicked.connect(self.generatedata)
        self.pushButton_file.clicked.connect(self.generatedatafile)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_mailfile.clicked.connect(self.addfile)
        self.pushButton_saveconfig.clicked.connect(self.saveconfig)
        self.pushButton_config.clicked.connect(self.config)

    # 清理临时文件并退出
    def exit_clear(self):
        shutil.rmtree('temporaryfile')
        os.mkdir('temporaryfile')
        exit()

    # 初始化界面，载入事先写好的值
    def gui_init(self):
        data_js = open('data/config.json', encoding='utf-8', mode='r')
        data = json.load(data_js)
        for name in data['API'].keys():
            self.comboBox_api.addItem(name)
        for name in data['User'].keys():
            self.comboBox_user.addItem(name)
        for name in data['method'].keys():
            self.comboBox_method.addItem(name)
        for name in data['edit'].keys():
            self.comboBox_edit.addItem(name)

    # 添加指定参数到config中，并更新GUI中值
    def add(self):
        edit_target = self.comboBox_edit.currentText()
        try:
            _ = self.textEdit_edit.toPlainText().split(':')
            edit_parameters, edit_value = _[0], _[1]
            data_js = open('data/config.json', encoding='utf-8', mode='r')
            data = json.load(data_js)
            print(self.comboBox_api.findText(edit_parameters))
            if edit_target == 'API' and self.comboBox_api.findText(edit_parameters) == -1:
                self.comboBox_api.addItem(edit_parameters)
            elif edit_target == 'User' and self.comboBox_user.findText(edit_parameters) == -1:
                self.comboBox_user.addItem(edit_parameters)
            data[edit_target][edit_parameters] = edit_value
            data_js = open('data/config.json', encoding='utf-8', mode='w')
            json.dump(data, data_js)
            data_js.close()
        except Exception as e:
            print(e)

    """
    # 添加object和params参数，参数名和值在两边一一对应，逐条添加到对应字典中
    def addparameter(self):
        par_switch = self.comboBox_parameters.currentText()
        parameters = self.textEdit_parameters.toPlainText()
        add_parameter(par_switch, parameters)
    """

    # 根据api更新TextBrowns中的文本，md存放在data文件夹中
    def updatetext(self):
        try:
            api = self.comboBox_api.currentText()
            md = open(f'data/{api}.md', encoding='utf-8', mode='r+')
            self.textEdit_info.setMarkdown(md.read())
        except Exception as e:
            self.textEdit_info.setText(str(e))

    # 删除指定参数，并更新GUI中值
    def dele(self):
        try:
            edit_target = self.comboBox_edit.currentText()
            _ = self.textEdit_edit.toPlainText()
            if edit_target == 'API' and self.comboBox_api.findText(_) != -1:
                self.comboBox_api.removeItem(self.comboBox_api.findText(_))
            elif edit_target == 'User' and self.comboBox_user.findText(_) != -1:
                self.comboBox_user.removeItem(self.comboBox_user.findText(_))
            data_js = open('data/config.json', encoding='utf-8', mode='r')
            data = json.load(data_js)
            data[edit_target].pop(_)
            data_js = open('data/config.json', encoding='utf-8', mode='w')
            json.dump(data, data_js)
            data_js.close()
        except Exception as e:
            print(e)

    # 查询参数
    def search(self):
        search_kind = self.comboBox_kinds.currentText()
        search_content = self.textEdit_search.toPlainText()
        data = search_data(search_kind, search_content)
        self.textEdit_search.setText("查询结果如下：\n")
        for item in data.items():
            self.textEdit_search.append(f"{item}\n")

    # 发送邮件
    def send(self):
        toaddrs = self.textEdit_recipients.toPlainText().split('\n')
        fileaddrs = self.textEdit_mailfile.toPlainText().split('\n')
        content = '你好，附件中有项目报告，请过目。\n' + self.textEdit_data.toPlainText()
        send_email_attach(toaddrs, content, fileaddrs)

    # 生成数据并显示在文本框中
    def generatedata(self):
        config_js = open("data/config.json", encoding="utf-8", mode="r")
        config_dict = json.load(config_js)
        api = self.textEdit_api.toPlainText()
        method = config_dict["method"][self.comboBox_method.currentText()]
        user = config_dict["User"][self.comboBox_user.currentText()]
        params = trans(self.textEdit_params.toPlainText().split('\n'))
        object = trans(self.textEdit_object.toPlainText().split('\n'))
        conditions = self.textEdit_condition.toPlainText().split('\n')
        backs = self.textEdit_back.toPlainText().split('\n')
        data = generate(api, method, user, params, object, conditions, backs)

        self.textEdit_data.clear()
        data_js = open("temporaryfile/data.json", encoding="utf-8", mode="w")
        json.dump(data, data_js)
        data_js.close()
        self.textEdit_data.textCursor().insertText("邮件正文：\n\n相关查询结果如下：\n")
        self.textEdit_data.textCursor().movePosition(QTextCursor.End)
        _table = self.textEdit_data.textCursor().insertTable(len(data) + 1, len(backs))
        statistic(_table, backs, data)

    # 生成数据并保存
    def generatedatafile(self):
        data_js = open("temporaryfile/data.json", encoding="utf-8", mode="r")
        data_list = json.load(data_js)
        try:
            filepath, type = QFileDialog.getSaveFileName(self, "文件保存", "temporaryfile", 'csv(*.csv)')
            f = open(filepath, encoding="utf-8", mode='w', newline='')
            csv_write = csv.writer(f)
            csv_write.writerow(data_list[0].keys())
            for row in data_list:
                csv_write.writerow(row.values())
            f.close()
        except Exception as e:
            print(e)

    # 自定义url
    def ensure(self):
        config_js = open("data/config.json", encoding="utf-8", mode="r")
        config_dict = json.load(config_js)
        self.textEdit_api.setText(config_dict['API'][self.comboBox_api.currentText()])

    # 为邮件添加文件
    def addfile(self):
        try:
            filepath, type = QFileDialog.getOpenFileName(self, "选择文件", "temporaryfile", 'csv(*.csv);;ALL Files(*)')
            if self.textEdit_mailfile.toPlainText() == '':
                self.textEdit_mailfile.setText(f'{filepath}')
            else:
                self.textEdit_mailfile.append(f'\n{filepath}')
        except Exception as e:
            print(e)

    # 保存配置
    def saveconfig(self):
        data = {
            'api': self.comboBox_api.currentText(),
            'url': self.textEdit_api.toPlainText(),
            'method': self.comboBox_method.currentText(),
            'user': self.comboBox_user.currentText(),
            'params': self.textEdit_params.toPlainText(),
            'object': self.textEdit_object.toPlainText(),
            'condition': self.textEdit_condition.toPlainText(),
            'back': self.textEdit_back.toPlainText(),
            'recipients': self.textEdit_recipients.toPlainText()
        }
        try:
            filepath, type = QFileDialog.getSaveFileName(self, "配置文件保存", "ConfigFile", 'json(*.json)')
            config = open(filepath, encoding="utf-8", mode='w')
            json.dump(data, config)
            config.close()
        except Exception as e:
            self.textEdit_edit.setText(str(e))

    # 初始化配置
    def config(self):
        try:
            filepath, type = QFileDialog.getOpenFileName(self, "选择配置文件", "ConfigFile", 'json(*.json)')
            config = open(filepath, encoding='utf-8', mode='r')
            data = json.load(config)
            self.comboBox_api.setCurrentText(data['api'])
            self.textEdit_api.setText(data['url'])
            self.comboBox_method.setCurrentText(data['method'])
            self.comboBox_user.setCurrentText(data['user'])
            self.textEdit_params.setText(data['params'])
            self.textEdit_object.setText(data['object'])
            self.textEdit_condition.setText(data['condition'])
            self.textEdit_back.setText(data['back'])
            self.textEdit_recipients.setText(data['recipients'])
        except Exception as e:
            self.textEdit_edit.setText(str(e))
