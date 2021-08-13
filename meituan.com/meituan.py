# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/21 10:19
@Software: PyCharm
@File    : meituan.py
url : https://cd.meituan.com/meishi/c17/pn2/ 需要登陆获取cookie的token2
参数p为url携带参数的拼接除token外
'''
import requests
import execjs

cookies = {
    'token2': 'iheXYU-c2VjZ34sUygVvONwzWxgAAAAAyQ0AAGsHPW3_b1FMESofS2va-Mw9js13rBHUHul3Jo4eQNKGZFnn6lV0Dzf9QOihqkuf5A',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cd.meituan.com/meishi/c17/pn2/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
with open('encrypt.js') as r:
    js_str = r.read()
p = f"https://cd.meituan.com/meishi/api/poi/getPoiList?cityName={'成都'}&cateId={17}&areaId={0}&sort=&dinnerCountAttrId=&page={2}&userId={197614759}&uuid={'6eb03a3a8006446c9765.1624009870.1.0.0'}&platform={1}&partner={126}&originUrl={'https://cd.meituan.com/meishi/c17/pn2/&riskLevel=1&optimusCode=10'}"

token = execjs.compile(js_str).call('get_token', p)
params = (
    ('cityName', '\u6210\u90FD'),
    ('cateId', '17'),
    ('areaId', '0'),
    ('sort', ''),
    ('dinnerCountAttrId', ''),
    ('page', '2'),
    ('userId', '197614759'),
    ('uuid', '6eb03a3a8006446c9765.1624009870.1.0.0'),
    ('platform', '1'),
    ('partner', '126'),
    ('originUrl', 'https://cd.meituan.com/meishi/c17/pn2/'),
    ('riskLevel', '1'),
    ('optimusCode', '10'),
    ('_token', f'{token}'),
)

response = requests.get('https://cd.meituan.com/meishi/api/poi/getPoiList', headers=headers, params=params,
                        cookies=cookies)
print(response.text)
