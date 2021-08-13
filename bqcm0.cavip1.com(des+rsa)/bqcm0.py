# -*- coding: utf-8 -*-
"""
url: https://bqcm0.cavip1.com/ 登录参数 password
"""
import execjs
import requests

session = requests.session()

with open('get_data.js', 'r', encoding='utf8')as f:
    js_code = f.read()

i = execjs.compile(js_code).call('get_rndString')

key = session.get('https://bqcm0.cavip1.com/wps/session/key/rsa').text
print(key)

encryption = execjs.compile(js_code).call('get_encryption', key, i)
print(encryption)

headers = {
    'authority': 'bqcm0.cavip1.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'merchant': 'changan818',
    'accept': '*/*',
    'encryption': encryption,
    'x-requested-with': 'XMLHttpRequest',
    'moduleid': 'COMM3',
    'content-type': 'application/json',
    'device': 'web',
    'origin': 'https://bqcm0.cavip1.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://bqcm0.cavip1.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_ga=GA1.2.1908259931.1624349829',
}

data = execjs.compile(js_code).call('get_data', i)
print(data)
response = session.post('https://bqcm0.cavip1.com/wps/session/login', headers=headers, data=data)
print(response.text)
