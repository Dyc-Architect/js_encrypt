# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/26 11:50
@Software: PyCharm
@File    : wsgjp.py
url :http://passport.wsgjp.com.cn/ clientinfo/password/userName
'''
import json

import requests
import execjs

with open('encrypt.js') as r:
    js_str = r.read()
username = 'dyc'
pwd = '123456'
encrypt_data = execjs.compile(js_str).call('encrypt', username, pwd)
userName = encrypt_data.get('userName')
password = encrypt_data.get('password')
clientinfo = encrypt_data.get('clientinfo')
cookies = {
    '_ga': 'GA1.3.479978912.1621913743',
    '_gid': 'GA1.3.1502142472.1621913743',
    'Qs_lvt_68170': '1621913741%2C1621942824',
    'Hm_lvt_1712ba79db147472df18b469e42780b8': '1621913741,1621942826',
    'Qs_pv_68170': '4489150891439860000%2C1991532639378034400%2C816759033205920800%2C1315128142293070800%2C1116276533879923000',
    'Hm_lpvt_1712ba79db147472df18b469e42780b8': '1621943246',
    'acw_tc': '276077ca16219449318444555e7f7a568bfcdf79c5507c73ca277d55029541',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'Content-Type': 'application/json',
    'Origin': 'http://passport.wsgjp.com.cn',
    'Referer': 'http://passport.wsgjp.com.cn/erp/login?productid=0',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
    'clientinfo': f"{clientinfo}",
    'companyName': "dyc",
    'host': "wsgjp.com.cn",
    'https': "false",
    'password': f"{password}",
    'productId': "14",
    'ref': "http://passport.wsgjp.com.cn/erp/login?productid=0",
    'rememberMe': 'false',
    'showNotice': 'true',
    'userName': f"{userName}",
    'validateCode': "",
}

response = requests.post('http://passport.wsgjp.com.cn/erp/login', headers=headers, cookies=cookies,
                         data=json.dumps(data), verify=False)

print(response.text)
