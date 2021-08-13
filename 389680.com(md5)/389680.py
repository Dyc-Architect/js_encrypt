# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/25 9:58
@Software: PyCharm
@File    : 389680.py
url: https://www.389680.com/ 登录密码和token
备注： 滑块验证码破解会返回validCode字段
'''
import hashlib

import requests


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


def encrypt(data):
    encrypt_data = encrypt_md5(encrypt_md5(data))
    m, n = encrypt_data[:16], encrypt_data[16:]
    x = ''.join(reversed(m)) + ''.join(reversed(n))
    y = x + x[:3]
    md5_data = encrypt_md5(y)
    return md5_data


url = 'https://www.389680.com/member/memberManager/login'
userAccount = 'wqeq'
userPassword = '123456'
data = {
    'userAccount': 'wqeq',
    'userPassword': f'{encrypt(userPassword)}',
    'userName': '',
    'registerSourceName': '389.so',
    'validCode': 't03ZRM5AHBwhbgHw_gSS5oa71h_pRRx3AeAelNyx1d-1j67sdfintCMloY5grr82vcCauQ4kppICLoKSQ6zGzA_w6m39BhY6Ahj22HmwGojVwphwtVVe4K-Pw**--@sfm',
    'token': f'{encrypt(userAccount)}',
}
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'deviceInfo': '{"mobile":"Edge 90.0.818.66","os":"Windows 90.0.818.66","browser":"Edge"}',
    'sec-ch-ua-mobile': '?0',
    'Authorization': '00929e8f-d062-4129-b9fc-e5cbc4f35ce9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.389680.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.389680.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
cookies = {
    'utoken': '00929e8f-d062-4129-b9fc-e5cbc4f35ce9',
}
resp = requests.post(url=url, headers=headers, cookies=cookies, data=data).text
print(resp)
