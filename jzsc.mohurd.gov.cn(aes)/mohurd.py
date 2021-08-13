# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/10 20:09
@Software: PyCharm
@File    : mohurd.py
url :http://jzsc.mohurd.gov.cn/data/company 数据解密
不成功是execjs的原因
'''
import requests
import execjs

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1620647617',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1620647639',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'timeout': '30000',
    'accessToken': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

response = requests.get('http://jzsc.mohurd.gov.cn/api/webApi/asite/qualapt/aptData', headers=headers, cookies=cookies,
                        verify=False)
with open('encrypt.js') as r:
    js_str = r.read()
print(response.content.decode())
data = execjs.compile(js_str).call('decrypt', response.content.decode())
print(data)
