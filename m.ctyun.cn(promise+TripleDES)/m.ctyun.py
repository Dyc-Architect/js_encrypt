# -*- coding: utf-8 -*-
"""
url: https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy 登录参数 password
"""
import execjs
import requests

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

userName = '123456@163.com'
password = '192837adg!'

with open('get_password.js', 'r', encoding='utf8')as f:
    js = f.read()
password = execjs.compile(js).call('encrypted', userName, password)
comParam_seqCode = execjs.compile(js).call('comParam_seqCode')
comParam_signature = execjs.compile(js).call('comParam_signature')


params = (
    ('userName', userName),
    ('password', password),
    ('referrer', 'wap'),
    ('mainVersion', '300021100'),
    ('comParam_curTime', '1624255328858'),
    ('comParam_seqCode', f'{comParam_seqCode}'),
    ('comParam_signature', f'{comParam_signature}'),
    ('isCheck', 'true'),
    ('locale', 'zh-cn'),
)

response = requests.get('https://m.ctyun.cn/account/login', headers=headers, params=params)
print(response.text)
