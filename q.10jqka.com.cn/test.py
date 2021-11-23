# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/11/23 15:30
@Software: PyCharm
@File    : test.py
'''
import re

import requests

import execjs

session = requests.session()
headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/5/ajax/1/code/301558",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
url = "http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/5/ajax/1/code/301175"
response = session.get(url, headers=headers, verify=False)
js_url = 'http:' + re.findall('src="(\S*?.js)"', response.text)[0]

resp = session.get(js_url).text
token_server_time = re.findall('TOKEN_SERVER_TIME=(\d+.\d+);', resp)[0]
with open('encrypt.js') as r:
    js_str = r.read()
cookie = execjs.compile(js_str).call('cookie', token_server_time)
cookies = {
    "v": f"{cookie}"
}
resp = session.get(url=url, headers=headers, cookies=cookies).text
print(resp)
