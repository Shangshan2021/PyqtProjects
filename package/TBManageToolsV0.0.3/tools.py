import json
import configparser
import os
import pyperclip
from datetime import datetime, timedelta


def saveDict(filePath, fileName, dic):
    json_data = json.dumps(dic)
    with open(filePath + '/' + fileName + '.json', mode='w', encoding='utf-8') as json_file:
        json_file.write(json_data)


def trans(string_list):
    dictionary = {}
    for string in string_list:
        if string == '':
            return dictionary
        pair = string.split(':')
        dictionary[pair[0]] = pair[1]
    return dictionary


# 读取配置文件
def getConfig(filename, section, option):
    """
    :param filename 文件名称
    :param section: 服务
    :param option: 配置参数
    :return:返回配置信息
    """
    # 获取当前目录路径
    proDir = os.path.split(os.path.realpath(__file__))[0]
    # print(proDir)

    # 拼接路径获取完整路径
    configPath = os.path.join(proDir, filename)
    # print(configPath)

    # 创建ConfigParser对象
    conf = configparser.ConfigParser()

    # 读取文件内容
    conf.read(configPath)
    config = conf.get(section, option)
    return config


def statistic(_table, backs, data):
    for i in range(0, len(backs)):
        _table.cellAt(0, i).firstCursorPosition().insertText(backs[i])
    dict_num = 1
    for item in data:
        for i in range(0, len(backs)):
            _table.cellAt(dict_num, i).firstCursorPosition().insertText(str(item[backs[i]]))
        dict_num += 1


def find_user(tb, user_name):
    users = \
        tb.general_function('https://open.teambition.com/api/org/member/list',
                            {'orgId': tb.company_id, 'pageSize': 500},
                            {}, 'GET',
                            tb.user_id).json()['result']
    for user in users:
        if user['name'] == user_name:
            return user['memberId'], True
    return '', False


def copy_in(data):
    pyperclip.copy(data)
    pyperclip.paste()


def getMethodList():
    file = open('./Config/Methods.json', encoding='utf-8', mode='r')
    methods = json.load(file)
    methods['其他_说明'] = 'https://www.cnblogs.com/yanyh-robot'
    file = open('./Config/Methods.json', encoding='utf-8', mode='w')
    json.dump(methods, file)
    data = list(methods.keys())
    return data

def init_mailbox():
    saveDict('./Config', 'recipients', {'王一先': 'yixian.wang@uwa4d.com', '张强': 'qiang.zhang@uwa4d.com','Add New Recipient':''})
    saveDict('./Config', 'senders', {'王一先': ['yixian.wang@uwa4d.com','Uwa666'],'Add New Sender':[]})


def data_format(data):
    """
    __TODO__:
    格式化数据，更易读取与保存
    :param data:
    :return:
    """
    return data


def fileinit(f):
    f.write('\n# 截至')
    f.write(str(datetime.now()))
    f.write('\n# Teambition自定义任务提醒')  # 报告头
    now_time = datetime.now()
    utc_time = now_time - timedelta(hours=8) - timedelta(days=7)
    limit_time = utc_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return limit_time