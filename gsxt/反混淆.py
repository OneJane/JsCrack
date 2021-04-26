import execjs

with open(r'第二次请求.js', encoding='utf-8', mode='r') as f:
    JsData = f.read()
cookie = execjs.compile(JsData).call('request')
print(cookie)