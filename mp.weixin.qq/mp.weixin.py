# -*- coding: utf-8 -*-
"""
url: https://mp.weixin.qq.com/ 登录参数 password
"""
import execjs
import requests

headers = {
    'referer': 'https://mp.weixin.qq.com/',
}

info = {
  'username': 'xxxxxxxx',
  'pwd': 'xxxxxxxxx'
}

with open('get_password.js', 'r')as f:
    js_code = f.read()

a = execjs.compile(js_code).call('test', info['pwd'])
print(a)
data = {
  'username': info['username'],
  'pwd': a,
  'imgcode': '',
  'f': 'json',
  'userlang': 'zh_CN',
  'redirect_url': '',
  'token': '',
  'lang': 'zh_CN',
  'ajax': '1'
}

response = requests.post('https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin', headers=headers, data=data)
print(response.text)
