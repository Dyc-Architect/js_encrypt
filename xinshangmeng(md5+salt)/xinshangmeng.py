# -*- coding: utf-8 -*-
"""
url: https://mp.weixin.qq.com/ 登录参数 j_mcmm
"""
import time

import execjs
import requests

username = 'xxxxxxxxx'
password = 'xxxx'
vcode = ''  # 验证码

with open('get_cookie.js', 'r')as f:
    js_code = f.read()

j_mcmm = execjs.compile(js_code).call('test', password, vcode)
print(j_mcmm)

params = (
    ('jsonp', 'jQuery99906012894814918179_1626341790413'),
    ('protocol', 'http:'),
    ('loginIndex', 'http://www.xinshangmeng.com/xsm2/?Version=2021061900'),
    ('j_mmrm', username),
    ('j_mcmm', '44160afa459e65befe0e7bb742dfdb53'),
    ('j_valcode', '2985'),
    ('_', int(time.time()*1000)),
)

res = requests.get('http://login.xinshangmeng.com/login/users/dologin/dfaup', params=params)
print(res.text)
