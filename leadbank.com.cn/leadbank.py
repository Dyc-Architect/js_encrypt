# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/20 17:40
@Software: PyCharm
@File    : leadbank.py
url : http://www.leadbank.com.cn/login/ data参数
'''
import execjs
import requests
import datetime

with open('encrypt.js') as r:
    js_str = r.read()

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
time = datetime.datetime.utcnow().strftime(GMT_FORMAT)
code = '123456'
phone = '15596870128'
password = '15596870128'
data_ = execjs.compile(js_str).call('J', time, phone, code, password)
cookies = {
    'Hm_lvt_54757a09f217c9eeabfe2492cf6ad31d': '1619156795,1621482168',
    'Hm_lpvt_54757a09f217c9eeabfe2492cf6ad31d': '1621482168',
    'user_token': '34b760b58cda4fc7bc8fabce27117511',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://www.leadbank.com.cn',
    'Referer': 'http://www.leadbank.com.cn/login/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
    'data': f'{data_}'
}

response = requests.post('http://www.leadbank.com.cn/front-gateway-web/quickLogin.app', headers=headers,
                         cookies=cookies, data=data, verify=False)

print(response.text)
