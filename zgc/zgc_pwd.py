import requests
from hashlib import md5

username = '15806204095'
pwd = '123'
md5_pwd = md5((pwd + 'zol').encode('utf8')).hexdigest()
print(md5_pwd)
url = 'https://service.zol.com.cn/user/ajax/siteLogin/login.php'
data = {
    'userid': username,
    'pwd': md5_pwd,
    'isAuto': '1',
    'backurl': 'http://www.zol.com.cn/',
    'tmallBtn': '0',
    'activeBtn': '0',
    'headPicid': '0',
}
r =requests.post(url,data)
print(r.text)
