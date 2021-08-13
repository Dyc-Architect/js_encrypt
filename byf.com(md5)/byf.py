# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/7 20:09
@Software: PyCharm
@File    : byf.py
url : http://www.byf.com/member/login.php password
'''
import hashlib

import requests


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


headers = {
    'Referer': 'http://www.byf.com/member/login.php',
}
username = "duyichuang"
password = '123456'
data = {
    'forward': 'http://www.byf.com/',
    'username': 'duyichuang',
    'password': f'{encrypt_md5(password)}',
    'submit': ' \u767B \u5F55 ',
    'cookietime': '1'
}

response = requests.post('http://www.byf.com/member/login.php', headers=headers, data=data, verify=False)
print(response.content.decode())
