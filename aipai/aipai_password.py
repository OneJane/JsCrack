import requests
import execjs

username = "15806204095"
password = "123"
with open(r'aipai_password.js', encoding='utf-8', mode='r') as f:
    JsData = f.read()
password = execjs.compile(JsData).call('pwd', password)
print(password)
data = {
    'action': 'loginNew',
    'user': username,
    'password': password,
    'keeplogin': '1',
    'comouterTime': '1',
    'userNowTime': '1618281089',

}
r = requests.post("http://www.aipai.com/login.php", data)
print(r.text)
