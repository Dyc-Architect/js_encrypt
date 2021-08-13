# -*- coding: utf-8 -*-
"""
url: https://mail.sohu.com/fe/#/login 登录参数 password
"""
import re
import hashlib

import execjs
import requests

session = requests.session()
headers = {
    'cookie': 'itssohu=true; reqtype=pc; SUV=210320172555UVPR; a=123',
}
response = session.get('https://v4.passport.sohu.com/i/cookie/common?callback=passport403_cb1623241226789', headers=headers)
response = session.get('https://v4.passport.sohu.com/i/jf/code?type=0')
b = response.text
a = execjs.compile('''function test(ssss) {
    document = {};
    return eval(ssss)
}''').call('test', b.replace('"', ''))

jv = re.search('jv=(.*?);', a).group(1)
session.cookies.set('jv', jv)


def encrypt_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


youxiang = 'xxxx@sohu.com'
mima = 'xxxx'


data = {
  'userid': youxiang,
  'password': encrypt_md5(mima),
  'appid': '101305',
  'callback': 'passport403_cb1623242750632'
}

response = session.post('https://v4.passport.sohu.com/i/login/101305', data=data)
print(response.text)
