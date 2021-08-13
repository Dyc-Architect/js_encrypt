# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/25 11:31
@Software: PyCharm
@File    : yhz566.py
url : http://yhz566.com/ 登录参数jsondata
'''
import hashlib

import requests
import execjs
from PIL import Image
from lxml import etree
import pytesseract


def encrypt_md5(data):
    data = data
    md5 = hashlib.md5()
    md5.update(data.encode())
    encrypt_data = md5.hexdigest()
    return encrypt_data


session = requests.session()
response = session.get('http://yhz566.com/')
html = etree.HTML(response.text)
img_url = 'http://yhz566.com/' + html.xpath('''//div[@class="eycrefreshBtn1601"]/img//@src''')[0].replace('.', '')
vvccookie = html.xpath('''//input[@id="vvccookie"]//@value''')[0].strip()
response = session.get(img_url)
with open('cap.jpg', 'wb') as w:
    w.write(response.content)
img = Image.open('cap.jpg')
Img = img.convert('L')
threshold = 120
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
photo = Img.point(table, '1')
photo.save("test2.jpg")
image = Image.open('test2.jpg')
check_code = pytesseract.image_to_string(image).strip()  # 解析图片

with open('encrypt.js') as r:
    js_str = r.read()

username, password, code, vvccookie = 'dyc', '123456', f'{encrypt_md5(check_code)}', f'{vvccookie}'

jsondata = execjs.compile(js_str).call('encrypt', username, password, code, vvccookie)
cookies = {
    'CGISESSID': '1451b094ddce7be8c89026d31018515b',
    'FGTServer': '2025455CAC81E99F0533A276929E823CACBE982FFFCF275D22AF9E4B374ACA',
    'Hm_lvt_ed750730e9d20094e129d81fde9a5171': '1621908929',
    'Hm_lpvt_ed750730e9d20094e129d81fde9a5171': '1621908929',
    '_ga': 'GA1.2.1866075394.1621908930',
    '_gid': 'GA1.2.1332304431.1621908930',
    '_gat_gtag_UA_173160987_1': '1',
    '_gat_gtag_UA_168224955_5': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://yhz566.com',
    'Referer': 'http://yhz566.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('controller', 'default'),
    ('action', 'login'),
)

data = {
    'flag': 'login',
    'jsondata_rsa': f'{jsondata}',
    'Submit': 'json',
    'v': 'n'
}

response = session.post('http://yhz566.com/', headers=headers, params=params, cookies=cookies, data=data, verify=False)
print(response.json())
