# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/7 14:51
@Software: PyCharm
@File    : aq_99.py
url : https://aq.99.com/V3/NDUser_Login.htm  登录流程
为解决部分： 图片验证码的识别
'''
import requests
import execjs

session = requests.session()
cookies = {
    'UserCookie': '7d21190660bd91b8dccf3070',
    'h': 'd4-0.02530s',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://aq.99.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('action', 'getticket'),
    ('bussiness', 'aq_login'),
    ('_', '1623033863538'),
)

response = session.get('https://checkcode.99.com/token', headers=headers, params=params, cookies=cookies)
ticket = response.json().get('ticket')

cookies = {
    'ASP.NET_SessionId': 'py2a5o45ypa3v5vhq0iuxo45',
    'UserCookie': '7d21190660bd91b8dccf3070',
    'h': 'd4-0.02530s',
}

params = (
    ('nduseraction', 'getverifycodestate'),
    ('verifycodetype', 'UserLogin'),
    ('bussiness', 'aq_login'),
    ('ticket', f'{ticket}'),
    ('SiteFlag', '995'),
    ('RND', '0.15717710823856046'),
    ('_', '1623033863539'),
)

response = session.get('https://aq.99.com/AjaxAction/AC_verifycode.ashx', headers=headers, params=params,
                        cookies=cookies)
VerifyToken = response.json().get('VerifyToken')
VerifyCodeUrl = response.json().get('VerifyCodeUrl')

code = VerifyCodeUrl  ## 需要识别验证码
print(code)
cookies = {
    'aqv3com': 'null',
    'ASP.NET_SessionId': 'py2a5o45ypa3v5vhq0iuxo45',
    'UserCookie': f'{VerifyToken}',
    'h': 'd4-0.36858s',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://aq.99.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://aq.99.com/V3/NDUser_Login.htm',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
  'Action': 'logout',
  'Business': 'common',
  'Rnd': '0.45223445501561343'
}

response = session.post('https://aq.99.com/V3/Handler/Default.ashx', headers=headers, cookies=cookies, data=data)
cookies = {
    'ASP.NET_SessionId': 'py2a5o45ypa3v5vhq0iuxo45',
    'UserCookie': f'{VerifyToken}',
    'h': 'd4-0.00747s',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://aq.99.com/V3/NDUser_Login.htm',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
pwd = '123456'
with open('encrypt.js') as r:
    js_str = r.read()
password = execjs.compile(js_str).call('getMD5Value', pwd)
aws = execjs.compile(js_str).call('obtainAwslHello')
params = (
    ('siteflag', '995'),
    ('nduseraction', 'login'),
    ('txtUserName', '15596870128'),
    ('txtPassword', f'{password}'),
    ('checkcode', f'{code}'),
    ('Rnd', '0.4929375061221566'),
    ('aws', f'{aws}'),
    ('_', '1623033863537'),
)

response = requests.get('https://aq.99.com/AjaxAction/AC_userlogin.ashx', headers=headers, params=params, cookies=cookies)

print(response.text)