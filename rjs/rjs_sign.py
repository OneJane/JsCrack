import json

import requests
import execjs

username = "15806204095"
psssword = "123"
with open(r'rjs_sign.js', encoding='utf-8', mode='r') as f:
    JsData = f.read()
sign = execjs.compile(JsData).call('request',username,psssword)
data = json.dumps({"platform":"wap","session_token":"","session_id":"","data":{"userName":username,"password":psssword},"sign":sign,"timestamp":1618153079455})
r =requests.post("https://m.rjs.com/japi/account/login.json",data)
print(r.text)