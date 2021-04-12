import requests
from hashlib import md5

username = '15806204095'
pwd = '123'
md5_pwd = md5(("veenike" + md5(pwd.encode('utf8')).hexdigest() + "veenike").encode("utf8")).hexdigest()
print(md5_pwd)
url = 'https://passport.lagou.com/login/login.json?jsoncallback=jQuery111306946515748870927_1618229101639&isValidate=true&username='+username+'&password=+'+md5_pwd+'+&request_form_verifyCode=&challenge=c3bebcad0648898aa58cb3f4dbf2f820&_=1618229101642'
r =requests.get(url)
print(r.text)
