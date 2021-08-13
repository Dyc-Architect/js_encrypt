# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/6 11:16
@Software: PyCharm
@File    : wangyi.py
'''
import requests
import execjs

url = 'https://music.163.com/weapi/w/login/cellphone?csrf_token='
# result = requests.post('http://127.0.0.1:3000/wangyi/get_params_encSecKey',
#                        data={"data": ['15202458535', '123456']}).json()
with open('wangyi.js') as r:
    js_str = r.read()
phone = ''
password = ''
result = execjs.compile(js_str).call('get_params_encSecKey', phone, password)
data = {
    'params': result.get('params'),
    'encSecKey': result.get('encSecKey')
}
print(requests.post(url=url, data=data).text)
