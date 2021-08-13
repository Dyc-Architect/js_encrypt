# -*- coding: utf-8 -*-
"""
url: https://one.pingan.com.cn/paone/index.html?appId=11045&originApp=true#/login 登录参数 loginPwd
"""
import re
import time

import execjs
import requests


session = requests.session()
ts = session.get(f'https://paicc-core.pingan.com.cn/paicc-core-web/webapi/getCurrentTimeMillis.do?_={int(time.time()*1000)}').text
print(ts)

res = session.get('https://paicc-core.pingan.com.cn/paicc-core-web/webapi/login.view?tabs=account&appId=11045').text
localEccX = re.search('var localEccX = "(.*?)";', res).group(1)
localEccY = re.search('var localEccY = "(.*?)";', res).group(1)

with open('get_pwd.js', 'r', encoding='utf8')as f:
    js_code = f.read()

loginPwd = execjs.compile(js_code).call('getSM2JSChgValue', 'j_password', ts, localEccX, localEccY)
print(loginPwd)
