# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/4 16:07
@Software: PyCharm
@File    : kanzhun.py
url : https://www.kanzhun.com/firm/interview/1nR-298~.html 返回数据解密 webpack 不成功是execjs的问题

'''
import requests
import execjs

headers = {
    'authority': 'www.kanzhun.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
    'reqsource': 'fe',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.kanzhun.com/firm/interview/1nR-298~.html',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'W_CITY_S_V=7; R_SCH_CY_V=10402; AB_T=abva; __c=1622526150; __g=-; __l=l=%2Fwww.kanzhun.com%2Ffirm%2Finterview%2F1nR-298~.html&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1622526150; acw_tc=0bcb2f2f16226361162696339e0360b60ccc339df71ace9a2fe41a9bb4e58e; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1622637111; __a=60531260.1619607782.1619607782.1622526150.11.2.10.11',
}

params = (
    ('b', 'lWSii_m3ScSzuBhp4R1qB2GjQuiqsdWstInnpE0ukw8~'),
    ('kiv', 'veYntnKCQ0HRBfhB'),
)

response = requests.get('https://www.kanzhun.com/api_to/ci/stat.json', headers=headers, params=params)
data = response.text
iv = 'veYntnKCQ0HRBfhB'
with open('encrypt.js', encoding='utf8') as r:
    js_str = r.read()

text = execjs.compile(js_str).call('getdata', data, iv)
print(text)