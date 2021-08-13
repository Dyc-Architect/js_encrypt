# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/10 10:13
@Software: PyCharm
@File    : yiban.py
url : https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F 登录密码
'''
import re
import execjs
import requests

params = (
    ('go', 'http://www.yiban.cn/'),
)
session = requests.session()
response = session.get('https://www.yiban.cn/login', params=params)
encrypt_params = re.findall('data-keys=[\"\']([\S\s]*)[\"\']\s*?data-keys-time=[\"\']([0-9.]*)[\"\']', response.text)
privateKey = encrypt_params[0][0]
keys_time = encrypt_params[0][1]
with open('encrypt.js') as r:
    js_str = r.read()
password = '123456'
password = execjs.compile(js_str).call('encrypt', password, privateKey)
data = {
  'account': 'buhechun@126.com',
  'password': f'{password}',
  'captcha': '',
  'keysTime': f'{keys_time}'
}
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.yiban.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}


response = session.post('https://www.yiban.cn/login/doLoginAjax', data=data, headers=headers)
print(response.json())



