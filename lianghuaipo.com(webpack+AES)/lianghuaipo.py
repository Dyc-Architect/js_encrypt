# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/6/18 17:48
@Software: PyCharm
@File    : lianghuaipo.py
url : https://www.lianghuaipo.com/#/listed_stock_list 返回数据加密
'''
import requests
import execjs

headers = {
    'authority': 'api.lianghuaipo.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.lianghuaipo.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.lianghuaipo.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'Hm_lvt_a93cbc5800037e73153633ace5e288ec=1624008186; io=pIYWbW4n0tIy-LHrAKIf; Hm_lpvt_a93cbc5800037e73153633ace5e288ec=1624008208',
}

data = {
  'now_page': '1',
  'page_cnt': '30',
  'filter[stock_industry]': '',
  'filter[stock_plate]': '',
  'filter[stock_sponsor]': '',
  'filter[stock_is_greenshoe]': '',
  'filter[stock_is_stone]': '',
  'filter[stock_is_callback]': '',
  'filter[first_hand_winning_rate][0]': '0',
  'filter[first_hand_winning_rate][1]': '100',
  'filter[winning_rate_substr]': '0',
  'filter[stock_margin_value]': '0',
  'filter[apply_people_num]': '0',
  'filter[market_cap]': '0',
  'filter[issuance_price][0]': '0',
  'filter[issuance_price][1]': '100',
  'filter[tag]': '0',
  'filter[listed_year]': '',
  'filter[gray_pct_change][0]': '-50',
  'filter[gray_pct_change][1]': '300',
  'filter[first_day_pct_change][0]': '-50',
  'filter[first_day_pct_change][1]': '300',
  'filter[total_pct_change][0]': '-50',
  'filter[total_pct_change][1]': '300'
}

response = requests.post('https://api.lianghuaipo.com/hk_ipo/get_paged_listed_stock_list', data=data).json()

data = response.get('data')

with open('encrypt.js') as r:
    js_str = r.read()
data = execjs.compile(js_str).call('get_data', data)
print(data)