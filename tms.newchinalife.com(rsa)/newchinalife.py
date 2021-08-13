# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/5/10 19:49
@Software: PyCharm
@File    : newchinalife.py
url : http://tms.newchinalife.com/ex/app/login/login.jsp 登陆密码
'''
import requests
from PIL import Image
import pytesseract
import execjs


session = requests.session()
cookies = {
    'ex_sessionid': 'ECCBB2E0D7C89A3C4D92B20B2D7F7B07',
    'sto-id-20480': 'AKKMKIMAJABP',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Referer': 'http://tms.newchinalife.com/ex/app/login/login.jsp',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('r', '0.22308850739288255'),
)

response = session.get('http://tms.newchinalife.com/ex/app/login/loginCheckcode.jsp', headers=headers, params=params, cookies=cookies, verify=False)
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
check_code = pytesseract.image_to_string(image)   # 解析图片
cookies = {
    'ex_sessionid': 'ECCBB2E0D7C89A3C4D92B20B2D7F7B07',
    'sto-id-20480': 'AKKMKIMAJABP',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://tms.newchinalife.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://tms.newchinalife.com/ex/app/login/login.jsp',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
with open('encrypt.js') as r:
    js_str = r.read()
j_password = execjs.compile(js_str).call('encrypt')
data = {
  'json': 'false',
  'j_password': f'{j_password}',
  'j_username': '123456',
  'checkcode': f'{check_code}'
}

response = session.post('http://tms.newchinalife.com/ex/j_spring_security_check', headers=headers, cookies=cookies, data=data, verify=False)
print(response.text)
