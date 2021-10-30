# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/10/30 15:45
@Software: PyCharm
@File    : chuzhou.py
'''
# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/10/30 13:42
@Software: PyCharm
@File    : test.py
'''
import re
import execjs
import requests
session = requests.session()

url = 'https://www.chuzhou.gov.cn/zxzx/jryw/index.html'
resp = session.get(url=url).text
_0x14e579 = re.findall("_0x14e579=\'(\S*?)\'", resp)[0]
_0x351708 = re.findall("_0x351708=\'(\S*?)\'", resp)[0]
with open('encrypt.js') as r:
    js_str = r.read()
result = execjs.compile(js_str).call('encrypt', _0x14e579, _0x351708)
re_url = f'https://www.chuzhou.gov.cn/WZWSREL3p4engvanJ5dy9pbmRleC5odG1s?wzwschallenge={result}'
session.get(url=re_url)
resp = session.get(url=url).text
print(resp)
