# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/22 14:51
@Software: PyCharm
@File    : waitwaitpay.py
url : https://static.waitwaitpay.com/web/sd_se/index.html#/ 返回数据加密（webpack）
'''
import requests
import execjs

headers = {
    'authority': 'api.waitwaitpay.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'x-device-system': 'Android_qq_web',
    'x-app-version': '',
    'sec-ch-ua-mobile': '?0',
    'x-location': 'null',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
    'x-channel': 'qq_web',
    'x-device-brand': '',
    'x-device-version': '',
    'x-device-model': '',
    'x-connection': 'wifi',
    'x-position': 'null,null',
    'x-device-id': 'gd7yeICg4XRz5YvgEz3dDPvV3lR0wIQ5',
    'accept': '*/*',
    'origin': 'https://static.waitwaitpay.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://static.waitwaitpay.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

response = requests.get('https://api.waitwaitpay.com/api/voucher_suppliers', headers=headers)

with open('encrypt.js', encoding='utf8') as r:
    js_str = r.read()
data = execjs.compile(js_str).call('data', response.text)

print(data)