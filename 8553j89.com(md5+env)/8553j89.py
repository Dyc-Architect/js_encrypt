# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/8 17:29
@Software: PyCharm
@File    : 8553j89.py
url :http://8553j89.com/index.html 密码 、 did
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


if __name__ == '__main__':
    session = requests.session()
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'http://8553j89.com',
        'Referer': 'http://8553j89.com/views/main.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    data = {"name": "Chrome(90.0.4430.93)", "osType": "web",
            "osData": {"guid": "getCrossStorageId fail!", "fingerprint": 1756458401, "os": "Windows(10)",
                       "cpu": "amd64",
                       "screen": "2560x1401", "pixelRatio": 1.5, "colorDepth": 24, "timezone": "中国标准时间",
                       "language": "zh-CN", "engine": "WebKit(537.36)"}}

    response = session.post('http://8553j89.com/v/user/device', headers=headers, data=json.dumps(data),
                            verify=False).json()
    did = response.get('did')
    password = '123456'
    data = {
        'r': '0.9371187871252944',
        'account': 'huibokun',
        'password': f'{encrypt_md5(password)}',
        'did': f'{did}'
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://8553j89.com',
        'Referer': 'http://8553j89.com/views/main.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    response = session.post('http://8553j89.com/v/user/sign_in', headers=headers, data=data, verify=False)
    print(response.text)
