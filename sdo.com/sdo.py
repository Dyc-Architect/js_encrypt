# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/20 11:27
@Software: PyCharm
@File    : sdo.py
url : https://login.u.sdo.com/sdo/Login/LoginSDO.php 密码
'''
import execjs
import requests
with open('encrypt.js') as r:
    js_str = r.read()


password = execjs.compile(js_str).call('login_rsa_encrypt','123456')
headers = {
    'authority': 'cas.sdo.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://login.u.sdo.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'CASCID=CID01B7D78A774E4C0A9371D863B5A05721',
}

params = (
    ('callback', 'staticLogin_JSONPMethod'),
    ('inputUserId', '15596870128'),
    ('password', f'{password}'),
    ('appId', '0'),
    ('areaId', '0'),
    ('serviceUrl', ''),
    ('productVersion', 'v5'),
    ('frameType', '3'),
    ('locale', 'zh_CN'),
    ('version', '21'),
    ('tag', '20'),
    ('authenSource', '2'),
    ('productId', '2'),
    ('scene', 'login'),
    ('usage', 'aliCode'),
    ('isEncrypt', '1'),
    ('autoLoginFlag', '0'),
    ('_', '1621480056722'),
)

response = requests.get('https://cas.sdo.com/authen/staticLogin.jsonp', headers=headers, params=params)
print(response.text)