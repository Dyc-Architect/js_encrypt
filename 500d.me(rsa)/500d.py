# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/20 11:04
@Software: PyCharm
@File    : 500d.py
url : https://www.500d.me/login/ 登陆密码
'''

import execjs
import requests

cookies = {
    'token': 'b41a6a7e-4785-4d16-a3bd-1ed2dbfd4a7c',
    'SESSION': '2e43944c-5d25-4d0d-a631-e4e64df76380',
}
params = (
    ('_', '1621479702306'),
)

response = requests.get('https://www.500d.me/common/public_key/', cookies=cookies)

modulus = response.json().get('modulus')
exponent = response.json().get('exponent')
with open('encrypt.js') as r:
    js_str = r.read()
password = '123456'
enpassword = execjs.compile(js_str).call('encrypt', modulus, exponent, password)

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
    'token': 'b41a6a7e-4785-4d16-a3bd-1ed2dbfd4a7c',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.500d.me',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.500d.me/login/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
  'username': 'duyichuang',
  'enPassword': f'{enpassword}',
  'service': '',
  'remember': 'true'
}

response = requests.post('https://www.500d.me/login/submit/', headers=headers, cookies=cookies, data=data)

print(response.text)
