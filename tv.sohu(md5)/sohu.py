# -*- coding: utf-8 -*-
"""
url: https://tv.sohu.com/ 手机登录参数 password
"""
import hashlib

import requests

username = 'xxxx'
password = 'xxxx'
md5 = hashlib.md5(password.encode())
password_encrypts = md5.hexdigest()
print(password_encrypts)

url = 'https://v4.passport.sohu.com/i/login/107405'
data = {
    'userid': username,
    'password': password_encrypts,
    'persistentCookie': 1,
    'appid': '107405',
    'callback': 'passport403_cb1619686078211'
}
res = requests.post(url, data=data)
print(res.text)
