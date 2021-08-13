# -*- coding: utf-8 -*-
"""
url: http://www.leadbank.com.cn/login/ 登录参数 data
"""
import execjs
import requests

custMobile = 'xxxxxxxxxxx'
password = '123456'
verifyCode = 'xxxxx'  # 验证码
with open('get_data.js', 'r')as f:
    js = f.read()
data_en = execjs.compile(js).call('test', custMobile, password, verifyCode)

data = {
    'data': data_en
}


cookies = {
    'user_token': '2dadf2934f1e45c588dacde50f91517a',
}

headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://www.leadbank.com.cn',
    'Referer': 'http://www.leadbank.com.cn/login/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


res = requests.post('http://www.leadbank.com.cn/front-gateway-web/login.app', headers=headers, cookies=cookies, data=data)

print(res.text)
