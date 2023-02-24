import argparse
import base64
import hashlib
import hmac
import json
import os
import requests
import time
from urllib.parse import quote_plus
from TBFunc import GetTeamBitionEvents, generate
from tools import fileinit,trans

class Messenger:
    def __init__(self, token=os.getenv("DD_ACCESS_TOKEN"), secret=os.getenv("DD_SECRET")):
        self.timestamp = str(round(time.time() * 1000))
        self.URL = "https://oapi.dingtalk.com/robot/send"
        self.headers = {'Content-Type': 'application/json'}
        secret = secret
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(self.timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        self.sign = quote_plus(base64.b64encode(hmac_code))
        self.params = {'access_token': token, "sign": self.sign}

    def send_text(self, content):
        """
        发送文本
        @param content: str, 文本内容
        """
        data = {"msgtype": "text", "text": {"content": content}}
        self.params["timestamp"] = self.timestamp
        return requests.post(
            url=self.URL,
            data=json.dumps(data),
            params=self.params,
            headers=self.headers
        )

    def send_md(self, title, content):
        """
        发送Markdown文本
        @param title: str, 标题
        @param content: str, 文本内容
        """
        data = {"msgtype": "markdown", "markdown": {"title": title, "text": content}}
        self.params["timestamp"] = self.timestamp
        return requests.post(
            url=self.URL,
            data=json.dumps(data),
            params=self.params,
            headers=self.headers
        )


def send_dingtalk(token,secret):
    markdown_text = "\n".join(open("log.md", encoding="utf-8").readlines())
    m = Messenger(
        token=token,
        secret=secret
    )
    m.send_md('日报', markdown_text)
    time.sleep(3)  # 发送完再删掉文件
    os.remove('log.md')


parser = argparse.ArgumentParser(description='Auto')
parser.add_argument('--config_path', default='', type=str)
args = parser.parse_args()
if args.config_path != '':
    args.config_path='tql1.json'
    tb = GetTeamBitionEvents()
    Config_file = open(args.config_path, encoding='utf-8', mode='r+')
    Config = json.load(Config_file)
    f = open('log.md', encoding="utf-8", mode='a')
    limit_time = fileinit(f)
    params = trans(Config['params'].split('\n'))
    object = trans(Config['object'].split('\n'))
    data = generate(Config['url'], Config['method'], Config['user'],params,object,
                    Config['condition'].split('\n'), Config['back'].split('\n'))
    f.write(f"\n> {Config['Note']}")
    for result in data:
        f.write('\n- ')
        if result['content']:
            f.write(result['content'])
    f.close()
    send_dingtalk(Config['dingTalk_token'],Config['dingTalk_secret'])
else:
    assert False, 'Please input right command.'



