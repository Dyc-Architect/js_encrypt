# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/7 19:59
@Software: PyCharm
@File    : yijianjiexi.py
url : http://www.yijianjiexi.com/ sign
'''
import requests
import time
import execjs

time = int(time.time())
link = "http://v.douyin.com/xYrtAo/"
md5_str = link + str(time)
with open('md5.js') as r:
    js_str = r.read()
sign = execjs.compile(js_str).call('g',md5_str)
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.yijianjiexi.com',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
  'link': 'http://v.douyin.com/xYrtAo/',
  'time': f'{time}',
  'sign': f'{sign}'
}

response = requests.post('http://www.yijianjiexi.com/ajax/index', headers=headers, data=data, verify=False)
print(response.content.decode())