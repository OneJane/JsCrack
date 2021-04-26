import hashlib
import re

import requests


def hex_md5(s):
    m = hashlib.md5()
    m.update(str(s).encode("utf-8"))
    return m.hexdigest()

headers = {
    'Host': 'passport.5173.com',
    'Origin': 'https://passport.5173.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.5173.com/?returnUrl=http%3A//www.5173.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
login_url = 'https://passport.5173.com/?returnUrl=http%3A//www.5173.com/'
html = requests.get(login_url).text
# print(html)
securityToken = re.findall('SecurityToken:"(.*?)",', html, re.M | re.S)[0]
passwordKey = re.findall('PasswordKey:"(.*?)",', html, re.M | re.S)[0]
print(passwordKey)
print(securityToken)


# 滑块 'https://passport.5173.com/Sso/ValidateSlide?token={}'.format(securityToken)
# hex_md5(hex_md5("123456").substr(8, 16) + "42m2gl")
password = hex_md5(hex_md5("123456")[8:8 + 16] + passwordKey)
userName = '15806204096'

data = {
    'smsLogin': '0',
    'userName': userName,
    'password': password,
    'mobileNo': '',
    'smsCaptcha': '',
    'category': '',
    'passpod': '',
    '__validationToken__': securityToken,
    '__validationDna__': ''
}
r = requests.post(login_url, data, headers=headers)
print(r.text)
