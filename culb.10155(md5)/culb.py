# -*- coding: utf-8 -*-
"""
url: http://club.10155.com/login 请求头参数 auth
"""
import time
import hashlib

import requests


def encrypt_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


userMobile = 'xxxxxxxxxxx'


date = time.strftime('%Y%m%d%H%M%S')
t = f'userMobile={userMobile}&timestamp={date}&appSecret=xsw21qaz'
auth = encrypt_md5(t)

headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '20210617111537',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'auth': f'woclub:{auth}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'http://club.10155.com',
    'Referer': 'http://club.10155.com/login/phone',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=490E52F69BC66BC93B9E13D37960515A; uuid=01000fdd814e40058fa8f58a9a6f2775; sessionId=267f5fffb05a8b71165b4416cad70d2b'
}

data = {
  'userMobile': userMobile
}

res = requests.post('http://club.10155.com/credit-member/sms/getsmscode', headers=headers, data=data)
print(res.text)
