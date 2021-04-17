import json
import requests
import execjs
import base64

from requests_toolbelt import MultipartEncoder

username = "15806204095"
psssword = "123456"
with open(r'jy_params.js', encoding='utf-8', mode='r') as f:
    JsData = f.read()
param = {"mobileNumber": "15806204095", "sendType": "reg", "channelId": 7, "channelCode": "J0005", "memberId": ""}
val = base64.b64encode(json.dumps(param).encode())
params = execjs.compile(JsData).call('getEncryption', val.decode())
print(params)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '341',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': 'JSESSIONID=DD188088D4E4EAC0098C9CCBCC32E52F; Hm_lvt_62d04228e1f84e012c1d9c0227f722c3=1618618136; Hm_lpvt_62d04228e1f84e012c1d9c0227f722c3=1618618136',
    'Host': 'www.jycinema.com',
    'Origin': 'http://www.jycinema.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.jycinema.com/wap/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36',
}
data = {'params': params}
r = requests.post("http://www.jycinema.com/frontUIWebapp/appserver/photoMessageService/newsSendMessage", data,
                  headers=headers)
print(r.text)
