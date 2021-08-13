# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/7 9:57
@Software: PyCharm
@File    : 5137.py
url : https://passport.5173.com/? 密码
不成功是因为缺少滑块验证
'''
import hashlib
import random
import re

import requests


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


if __name__ == '__main__':
    session = requests.session()
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://passport.5173.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://passport.5173.com/?',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    url = 'https://passport.5173.com/?'
    text = session.get(url=url).text
    PasswordKey = re.findall('PasswordKey\s*?:[\"\'](\S*?)[\"\']', text)[0]
    SecurityToken = re.findall('SecurityToken\s*?:\s*?[\"\'](\S*?)[\"\']', text)[0]
    # SecurityToken = '63807bdee4f14490a5712b2de0df639b'
    params = (
        ('token', '{}'.format(SecurityToken)),
    )
    x = random.randint(10, 20)
    y = random.randint(80, 90)
    z = random.randint(20, 30)
    data = f'{{"x":18,"y":-128,"t":1620386554222,"vs":[{x},-124,{y},{z},-115,91,28,-118,99,34,-120,107,44,-122,115,58,-124,123,75,-128,132,96,-131,140,120,-132,148,145,-132,156,167,-132,164,192,-132,171,211,-132,236,303,-128,237,312,-128,276,332,-128,277,333,-128,317,338,-128,317,343,-128,360,344,-128,363,345,-128,371,346,-128,379,347,-128,387,348,-128,395,348,-128,411,349,-128,419,350,-128,508,351,-128,531,352,-128,543,352,-128,547]}}'
    requests.post('https://passport.5173.com/Sso/ValidateSlide', headers=headers, params=params, data=data)
    password = encrypt_md5(encrypt_md5('123456')[8:16] + PasswordKey)
    data = {
        'smsLogin': '0',
        'userName': '15596870128',
        'password': '{}'.format(password),
        'mobileNo': '',
        'smsCaptcha': '',
        'category': '',
        'passpod': '',
        '__validationToken__': '{}'.format(SecurityToken),
        '__validationDna__': ''
    }
    response = requests.post('https://passport.5173.com/', data=data, headers=headers)
    print(response.text)