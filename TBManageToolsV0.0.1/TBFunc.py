from datetime import datetime, timedelta
import time
import jwt
import requests

from Config import getConfig

# 获取Teeambition数据
class GetTeamBitionEvents(object):

    def __init__(self):
        self.app_id = getConfig('config', 'Main', 'app_id')
        self.app_secret = getConfig('config', 'Main', 'app_secret')
        self.company_url = 'https://www.teambition.com/organization/'
        self.company_id = getConfig('config', 'Main', 'company_id_UWA')
        self.callback_url = self.company_url + self.company_id
        self.user_id = getConfig('config', 'Main', 'user_id')
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

    def post_project(self):
        url = f'https://open.teambition.com/api/project/query'
        app_token = (self.get_aptoken()).replace("\n", "").replace('\r', '')
        headers = {
            'x-operator-id': self.user_id,
            'Authorization': 'Bearer %s' % app_token,
            'X-Tenant-Id': '%s' % self.company_id,
            'X-Tenant-Type': 'organization'
        }
        object = {
            'pageSize': 4000,
            'orgId': self.company_id
        }
        return requests.post(url, json=object, headers=headers)

    def general_function(self, url, params, object, method,user='63310bc0b2b7b2cf2ca8a3b2'):
        app_token = (self.get_aptoken()).replace("\n", "").replace('\r', '')
        headers = {
            'x-operator-id': user,
            'Authorization': 'Bearer %s' % app_token,
            'X-Tenant-Id': '%s' % self.company_id,
            'X-Tenant-Type': 'organization'
        }
        if method == 'get' or method == 'GET':
            return requests.get(url, params=params, json=object, headers=headers)
        elif method == 'post' or method == 'POST':
            return requests.post(url, params=params, json=object, headers=headers)
        elif method == 'PUT' or method == 'put':
            return requests.put(url, params=params, json=object, headers=headers)
        elif method == 'del' or method == 'DEL':
            return requests.delete(url, params=params, json=object, headers=headers)