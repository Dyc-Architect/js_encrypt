# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/7 10:40
@Software: PyCharm
@File    : cls.py
url : https://www.cls.cn 密码 、sign
'''
import hashlib
import json

import requests


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


def encrypt_sha1(data):
    sha1 = hashlib.sha1(data.encode())
    encrypt_data = sha1.hexdigest()
    return encrypt_data


if __name__ == '__main__':
    sign = encrypt_md5(encrypt_sha1('app=CailianpressWeb&os=web&sv=7.5.5'))
    url = 'https://www.cls.cn/v1/user/login'
    password = encrypt_md5('123456')
    data = {
        "app": "CailianpressWeb",
        "captcha": "",
        "login_type": 1,
        "os": "web",
        "password": "{}".format(password),
        "phone": "15596870117",
        "sv": "7.2.2",
    }
    params = {
        'app': 'CailianpressWeb',
        'os': 'web',
        'sv': '7.5.5',
        'sign': '{}'.format(sign)
    }
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.cls.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.cls.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    resp = requests.post(url=url, data=json.dumps(data), headers=headers, params=params).content.decode()
    print(resp)
