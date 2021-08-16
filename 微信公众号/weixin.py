# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/8/16 10:27
@Software: PyCharm
@File    : weixin.py
'''
import re
import time
import requests
import hashlib


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


session = requests.session()
headers = {
    'authority': 'mp.weixin.qq.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://mp.weixin.qq.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://mp.weixin.qq.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}


def login(username, password):
    params = (
        ('action', 'startlogin'),
    )
    data = {
        'username': f'{username}',
        'pwd': f'{password}',
        'imgcode': '',
        'f': 'json',
        'userlang': 'zh_CN',
        'redirect_url': '',
        'token': '',
        'lang': 'zh_CN',
        'ajax': '1'
    }
    response = session.post('https://mp.weixin.qq.com/cgi-bin/bizlogin', headers=headers, params=params, data=data)
    bizuin = response.cookies.get('bizuin')
    cert = response.cookies.get('cert')
    fake_id = response.cookies.get('fake_id')
    login_certificate = response.cookies.get('login_certificate')
    login_sid_ticket = response.cookies.get('login_sid_ticket')
    ticket = response.cookies.get('ticket')
    ticket_certificate = response.cookies.get('ticket_certificate')
    ticket_id = response.cookies.get('ticket_id')
    ticket_uin = response.cookies.get('ticket_uin')
    uuid = response.cookies.get('uuid')
    return bizuin, cert, fake_id, login_certificate, login_sid_ticket, ticket, ticket_certificate, ticket_id, ticket_uin, uuid


def get_erweima(bizuin, cert, fake_id, login_certificate, login_sid_ticket, ticket, ticket_certificate, ticket_id,
                ticket_uin, uuid):
    headers[
        'cookie'] = f'bizuin={bizuin};cert={cert};fake_id={fake_id};login_certificate={login_certificate};login_sid_ticket={login_sid_ticket};ticket={ticket};ticket_certificate={ticket_certificate};ticket_id={ticket_id};ticket_uin={ticket_uin};uuid={uuid}'
    params = (
        ('action', 'getqrcode'),
        ('param', '4300'),
        ('rd', '854'),
    )
    response = session.get('https://mp.weixin.qq.com/cgi-bin/loginqrcode', headers=headers, params=params)
    with open('erweima.png', 'wb') as w:
        w.write(response.content)


def check_success():
    data = {
        'userlang': 'zh_CN',
        'redirect_url': '',
        'token': '',
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1'
    }
    params = (
        ('action', 'login'),
    )
    response = session.post('https://mp.weixin.qq.com/cgi-bin/bizlogin', headers=headers, params=params, data=data)
    data_bizuin = response.cookies.get('data_bizuin')
    data_ticket = response.cookies.get('data_ticket')
    slave_sid = response.cookies.get('slave_sid')
    slave_user = response.cookies.get('slave_user')
    redirect_url = response.json().get('redirect_url')
    token = re.findall('token=(\d+)', redirect_url)[0]
    headers[
        'cookie'] = f'data_bizuin={data_bizuin};data_ticket={data_ticket};slave_sid={slave_sid};slave_user={slave_user}'
    params = (
        ('t', 'home/index'),
        ('lang', 'zh_CN'),
        ('token', f'{token}'),
    )
    session.get('https://mp.weixin.qq.com/cgi-bin/home', headers=headers, params=params)
    return token


def get_article(token):
    fakeid_url = f"https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&begin=0&count=5&query=wind资讯&token={token}&lang=zh_CN&f=json&ajax=1"
    res = session.get(fakeid_url, headers=headers)
    lists = res.json().get('list', [])
    fakeid = lists[0].get('fakeid')
    data_url = f"https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid={fakeid}&type=9&query=&token={token}&lang=zh_CN&f=json&ajax=1"
    response = session.get(data_url, headers=headers)
    print(response.json())


def run():
    password = encrypt_md5('mimaXXXXXX')
    username = 'XXXXXXXX'
    bizuin, cert, fake_id, login_certificate, login_sid_ticket, ticket, ticket_certificate, ticket_id, ticket_uin, uuid = login(
        username, password)
    get_erweima(bizuin, cert, fake_id, login_certificate, login_sid_ticket, ticket, ticket_certificate, ticket_id,
                ticket_uin, uuid)
    time.sleep(20)
    token = check_success()
    get_article(token)


if __name__ == '__main__':
    run()
