# -*- coding: utf-8 -*-
"""
url: https://login.u.sdo.com/sdo/Login/LoginSDO.php 登录参数 password
"""
import time

import execjs
import requests

headers = {
    'authority': 'cas.sdo.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://login.u.sdo.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
}
inputUserId = 'xxxxxxxxxxx'
password = '123456'
with open('get_password.js', 'r')as f:
    js = f.read()
password = execjs.compile(js).call('login_rsa_encrypt', password)
print(password)

tt = int(time.time()*1000)
url = f'https://cas.sdo.com/authen/staticLogin.jsonp?callback=staticLogin_JSONPMethod&inputUserId={inputUserId}&password={password}&appId=0&areaId=0&serviceUrl=&productVersion=v5&frameType=3&locale=zh_CN&version=21&tag=20&authenSource=2&productId=2&scene=login&usage=aliCode&isEncrypt=1&autoLoginFlag=0&_={tt}'


res = requests.get(url, headers=headers)
print(res.text)
