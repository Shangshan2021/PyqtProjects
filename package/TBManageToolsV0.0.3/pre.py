from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from tools import saveDict


def getMethods():
    browser = webdriver.Chrome()
    browser.get('https://open.teambition.com/docs/documents/5d89a927a55fbd000120c30c')
    # 等待浏览器响应
    time.sleep(2)
    path = '/html/body/div/div/div/section/div[3]/div/div[4]/div[1]'
    # 获取API元素
    api = browser.find_element(By.XPATH, path)
    # 点击以展开
    api.click()
    # 等待浏览器响应
    time.sleep(2)
    # 获取API条目下所有类别条目（因为class的重复使用，所以后面会再次处理）
    category = browser.find_elements(By.CLASS_NAME, '_item-content_17591_121')
    dic_api = {}
    subclass = ''
    for i in category:
        if '\n' not in i.text:
            subclass = i.text
        if i.text == 'API' or i.text == '快速开始':
            continue
        elif i.text == '通讯录' or i.text == '历史版本（不推荐）':
            i.click()
            for subitem in i.find_elements(By.CLASS_NAME, '_item-text_17591_173'):
                if subitem.text == i.text:
                    continue
                else:
                    subitem.click()
                    if 'api' in browser.current_url and '\n' in i.text:
                        dic_api[subclass + '_' + subitem.text.split('\n')[1]] = browser.current_url
        else:
            i.click()
            if 'api' in browser.current_url and '\n' in i.text:
                dic_api[subclass + '_' + i.text.split('\n')[1]] = browser.current_url
    saveDict('./Config', 'Methods', dic_api)


getMethods()
