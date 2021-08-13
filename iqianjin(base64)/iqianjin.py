# -*- coding: utf-8 -*-
"""
url: https://www.iqianjin.com/user/login 登录参数 password
"""
import base64
import requests

name = 'xxxxx'
password = 'xxxxxx'


def base64(password):
    return base64.b64encode(password.encode("utf8")).decode()

data = {
  'name': name,
  'password': base64(password),
  'code': 'xxxxxxxx',  # 验证码
  'rememberMe': 'on'
}

response = requests.post('https://www.iqianjin.com/user/logon', data=data)
