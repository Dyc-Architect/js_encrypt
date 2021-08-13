# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/10 9:36
@Software: PyCharm
@File    : imooc.py
url : https://class.imooc.com/ 登陆密码和browser_key
'''
import requests

import execjs


headers = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Origin': 'https://class.imooc.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://class.imooc.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

response = requests.post('https://class.imooc.com/passport/user/prelogin', headers=headers).json()
code = response.get('code')
servertime = response.get('servertime')
a = f"{code}\t{servertime}\t123456"
with open('encrypt.js') as r:
    js_str = r.read()
password = execjs.compile(js_str).call('decrypt', a)
browser_key = execjs.compile(js_str).call('browser_key')
data = {
  'username': '15596870128',
  'password': f'{password}',
  'verify': '',
  'remember': '1',
  'pwencode': '1',
  'browser_key': f'{browser_key}',
  'referer': 'https://class.imooc.com'
}

response = requests.post('https://class.imooc.com/passport/user/login', data=data)
print(response.json())
