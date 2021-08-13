# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/10 10:19
@Software: PyCharm
@File    : iesdouyin.py
url : https://v.douyin.com/WqMX9d/
'''
import requests
import execjs

headers = {
    'authority': 'www.iesdouyin.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'accept': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.iesdouyin.com/share/user/110567353301?u_code=15a1f9f4g&sec_uid=MS4wLjABAAAABoLxMOoHpqPYizYAlLhaAjNp9lC4LLGE7uJdNAsKwj8&timestamp=1584612666&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': '_tea_utm_cache_1243={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; MONITOR_WEB_ID=ecbcb747-120c-4a65-9fb0-3b68c87b87d9',
}
with open('encrypt.js', encoding='utf8') as r:
    js_str = r.read()
_signature = execjs.compile(js_str).call('get_sign', '110567353301')
params = (
    ('sec_uid', 'MS4wLjABAAAABoLxMOoHpqPYizYAlLhaAjNp9lC4LLGE7uJdNAsKwj8'),
    ('count', '21'),
    ('max_cursor', '0'),
    ('aid', '1128'),
    ('_signature', 'a4nYuQAAC0qBwq7lrUJkG2uJ2K'),
    ('dytk', ''),
)

response = requests.get('https://www.iesdouyin.com/web/api/v2/aweme/post/', headers=headers, params=params)

print(response.text)