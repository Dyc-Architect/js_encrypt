# -*- coding: utf-8 -*-
"""
url: http://wwww-caipiao500.com/login 登录参数 password
"""
import execjs
import requests

with open('get_password.js', 'r')as f:
    js_code = f.read()

info = {
    "userName": "xxxxxxxxxxx",
    "password": "xxxxxxxx"
}

js = execjs.compile(js_code).call('test', info)
print(js)

data = {
  'userName': info['userName'],
  'password': js['password'],
  'random': js['random']
}

response = requests.post('http://77cai500.vip:3064/v1/users/login', data=data)
print(response.text)
