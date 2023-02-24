from datetime import datetime, timedelta
import time
import jwt
import requests
from tools import getConfig,find_user


# 获取Teeambition数据
class GetTeamBitionEvents(object):

    def __init__(self):
        ConfigPath='./Config/config'
        self.app_id = getConfig(ConfigPath, 'Main', 'app_id')
        self.app_secret = getConfig(ConfigPath, 'Main', 'app_secret')
        self.company_url = 'https://www.teambition.com/organization/'
        self.company_id = getConfig(ConfigPath, 'Main', 'company_id_UWA')
        self.callback_url = self.company_url + self.company_id
        self.user_id = getConfig(ConfigPath, 'Main', 'user_id')
        self.page_size = 4000

    def time_handler(self, target_time):
        """
        UTC世界标准时间（包含T和Z） 转 北京时间
        """
        date = datetime.strptime(target_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        local_time = date + timedelta(hours=8)
        end_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
        return end_time

    def get_aptoken(self):
        now_time = int(time.time())
        expire_time = now_time + 36000  # 1 小时后超时
        token_dict = {'iat': now_time,
                      '_appId': '%s' % self.app_id,
                      'exp': expire_time,
                      }
        headers = {
            'typ': 'jwt',
            'alg': 'HS256'
            # 声明所使用的算法
        }
        encoded = jwt.encode(payload=token_dict, key=self.app_secret, headers=headers,
                             algorithm='HS256')  # .decode('ascii')
        return encoded

    def general_function(self, url, params, object, method, user='63310bc0b2b7b2cf2ca8a3b2'):
        app_token = (self.get_aptoken()).replace("\n", "").replace('\r', '')
        headers = {
            'x-operator-id': user,
            'Authorization': 'Bearer %s' % app_token,
            'X-Tenant-Id': '%s' % self.company_id,
            'X-Tenant-Type': 'organization'
        }
        if method == 'get' or method == 'GET':
            return requests.get(url, params=params, json=object, headers=headers,verify=False)
        elif method == 'post' or method == 'POST':
            return requests.post(url, params=params, json=object, headers=headers,verify=False)
        elif method == 'PUT' or method == 'put':
            return requests.put(url, params=params, json=object, headers=headers,verify=False)
        elif method == 'del' or method == 'DEL':
            return requests.delete(url, params=params, json=object, headers=headers,verify=False)


def generate(api, method, user, params, object, conditions, backs,nextpage_token=None):
    tb = GetTeamBitionEvents()
    if 'pageSize' not in object.keys():
        object['pageSize']=50
    if nextpage_token is not None:
        object['pageToken']=nextpage_token
    user_id,exist=find_user(tb,user)
    if not exist:
        return ['未找到该公司成员']
    results = tb.general_function(api, params, object, method, user_id).json()
    if 'nextPageToken' in results.keys():
        nextPageToken=results['nextPageToken']
    else:
        nextPageToken=None
    if 'count' in results.keys():
        count=results['count']
    else:
        count=1
    results=results['result']
    for condition in conditions:
        data = []
        if condition == '':
            break
        condition_list = condition.split(':')
        if condition_list[1] == 'IN':
            for result in results:
                if condition_list[0] in str(result[condition_list[2]]):
                    data.append(result)
                else:
                    continue
        elif condition_list[1] == 'NOTIN':
            for result in results:
                if condition_list[0] not in str(result[condition_list[2]]):
                    data.append(result)
                else:
                    continue
        results = data
    data = []
    for result in results:
        result_dict = {}
        for back in backs:
            result_dict[back] = result[back]
        data.append(result_dict)
    return data,nextPageToken,count

