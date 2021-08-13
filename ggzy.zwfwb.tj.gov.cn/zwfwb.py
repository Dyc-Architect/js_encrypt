# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/8 16:45
@Software: PyCharm
@File    : zwfwb.py
url :http://ggzy.zwfwb.tj.gov.cn/jyxx/index.jhtml 详情页链接
'''
import requests
import re
import execjs

url = 'http://ggzy.zwfwb.tj.gov.cn/jyxx/index.jhtml'
resp = requests.get(url=url).text
detail_url = re.findall('url\s*?\=\s*?[\"\'](http://ggzy.zwfwb.tj.gov.cn:80/jyxxcggg/\d+\.jhtml)[\"\']{0,1}', resp)[0]
with open('encrypt.js') as r:
    js_str = r.read()
detail_url = execjs.compile(js_str).call('Decrypt',detail_url)
resp = requests.get(detail_url).text
print(resp)