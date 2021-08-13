# -*- coding: utf-8 -*-
"""
url: https://passport.kongzhong.com/ 登录参数 password
"""
import re
import time

import execjs
import requests


username = '13269619918'
password = '123456'

cookies = {
    'KSPSSIONID': '5E86173059FB32086D8B6DF07B2CE4C1',
}

headers = {
    'Referer': 'https://passport.kongzhong.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

res = requests.get('https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/', headers=headers)
dc = re.search('"dc":"(.*?)"', res.text).group(1)

with open('get_password.js', 'r')as f:
    js_code = f.read()

password = execjs.compile(js_code).call('test', password, dc)
vcode = 'xxxx'  # 验证码

param = f'&type=1&service=https://passport.kongzhong.com/&username={username}&password={password}&vcode={vcode}&toSave=0&_={int(time.time()*1000)}'
print(param)

url = 'https://sso.kongzhong.com/ajaxLogin?j=j&'+param
res = requests.get(url, headers=headers, cookies=cookies)
print(res.text)
