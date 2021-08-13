# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/4 16:15
@Software: PyCharm
@File    : jdj007.py
url : https://www.jdj007.com/ 请求参数加密 webpack
'''
import time

import requests
import execjs

with open('encrypt.js') as r:
    js_str = r.read()
timestamp = int(time.time() * 1000)

str1 = "timestamp=" + str(timestamp) + "&secret=aHVheWluZ19zZWNyZXRfYXBp"
sign = execjs.compile(js_str).call('getsign', str1)

headers = {
    'authority': 'www.jdj007.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.jdj007.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'Hm_lvt_41f295d2e70c8ca2935f404f3762f872=1622513965; Hm_lpvt_41f295d2e70c8ca2935f404f3762f872=1622794541',
}
response = requests.get(f'https://www.jdj007.com/api/article/type?timestamp={timestamp}&sign={sign}', headers=headers)
print(response.text)
