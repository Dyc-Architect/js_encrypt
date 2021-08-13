# -*- coding: utf-8 -*-
"""
url: https://www.doyo.cn/passport/login 登录参数 password
"""
import random
import hashlib

import requests

username = 'xxxx'
password = 'xxxx'
url = f'https://www.doyo.cn/User/Passport/token?username={username}&random={random.random()}'
res = requests.get(url).json()
nonce = res['nonce']
ts = res['ts']
sha = hashlib.sha1(password.encode())
encrypts = sha.hexdigest()
sha = hashlib.sha1(f'{nonce}{ts}{encrypts}'.encode())
password_encrypts = sha.hexdigest()


url = 'https://www.doyo.cn/User/Passport/login'
data = {
    'username': username,
    'password': password_encrypts,
    'remberme': 1,
    'next': 'JTJG'
}
res = requests.post(url, data=data)
print(res.json())
