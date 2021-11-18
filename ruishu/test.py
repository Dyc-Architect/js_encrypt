# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/11/18 13:40
@Software: PyCharm
@File    : test.py
说明：半成品吧!!!!!!!!
1 、执行win = execjs.compile(js_win).call('get_window', content)报错，不知道为啥，去section_1.js中调用get_window就正常
2、该自动那个脚本生成的cookie较短，ruishu2.js执行的cookie才是正常长度（最开始是在ruishu2中调试补得环境，改动了js代码，但是忘记改动哪里了，导致自动化脚本执行的cookie长度不对
，想研究可以两个对照这研究一下）
'''
import re
import execjs
import requests
url = 'http://www.customs.gov.cn/customs/302249/302274/302277/302276/1899449/index.html'
session = requests.session()
resp = session.get(url).text
content = re.findall('content="(\S*?)">', resp)[0]
js_str = re.findall('<script type="text/javascript" r="m">(\([\S\s]*?\))</script>', resp)[0]
call_str = re.findall('ret\s*?=\s*?\_\$\S*?\.call\(\S*?,\S*?\)', resp)[0]
_str = re.findall('ret\s*?=\s*?\_\$\S*?\.call\((\S*?,\S*?)\)', call_str)[0].split(',')
str1, str2 = _str[0], _str[1]
print(content)
js_str_ = js_str.replace(call_str, f'window._$Tv={str1};window._$Pp = {str2};ret = "";')
with open('def_window.js') as r:
    win = r.read()
with open('get_window.js') as r:
    get_win = r.read()
write_section_1 = win + js_str_ + '\n'+ get_win
with open('section_1.js', 'w') as w:
    w.write(write_section_1)
with open('section_1.js') as r:
    js_win = r.read()
win = execjs.compile(js_win).call('get_window', content)

with open('section_2.js') as r:
    cookie_str = r.read()
cookie = execjs.compile(cookie_str).call('getcookie')
session.cookies.update(cookie)
resp = session.get(url).text
print(resp)

