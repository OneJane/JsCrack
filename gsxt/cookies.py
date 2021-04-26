import execjs
import requests
import regex as re
import js2py

index_url = 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
# 获取request的session对象, 可以自动合并cookie信息
session = requests.session()
session.headers = headers

# ######################################################使用session发送index_url请求###########################
response = session.get(index_url)
print(response.status_code)
# 第一次请求521 服务器借助这个请求设置一个Set-Cookie: __jsluid_h=8af7a39f7cdb1c46f8f624c972968c8f; max-age=31536000; path=/; HttpOnly到本地，并返回一段js
print(session.cookies)
########################################################拿到第一个cookie########################
# 1. 提取script标签中的js
js1 = re.findall('<script>(.+?)</script>', response.content.decode())[0].replace('document.cookie=', '').replace(
    'location.href=location.pathname+location.search', '')
print(js1)
context = js2py.EvalJs()
###################################################根据第一个请求返回的js生成第二个cookie###############################
context.execute('cookies2 =' + js1)
cookies = context.cookies2.split(';')[0].split('=')
session.cookies.set(cookies[0], cookies[1])  # 到此拿到第两个cookie
print(session.cookies)
######################################################拿到第二个cookie############################


# 第二次请求携带Cookie: __jsluid_h=6ed2648e0a734bc66e3011d648f6f1ab; __jsl_clearance=1619152879.013|-1|aS3lFknWlGtD%2FADiygf7vxl4yqk%3D返回一段js
# 添加jsdom实现浏览器上下文
js2 = '''const jsdom = require("jsdom");const {JSDOM} = jsdom;const dom = new JSDOM();window = dom.window;document = window.document;location = new Array();''' + \
      re.findall('<script>(.+?)</script>', session.get(index_url).content.decode('utf-8'))[0]
# 正则获取document['cookie']，由于每次个数不一样我们取最后一个
cookies2_1 = re.findall(r"document\[.*?\]=(.*?)location", js2, re.S)[-1]
# 将document['cookie']内容返回给go函数
js3 = re.sub("};go", "return " + cookies2_1 + "};go", js2, 1)
# 获取调用go函数时里面的参数
request = re.findall(r"go\({(.*?)}\)", js3, re.S)[-1]
# 通过python修改js生成一个request方法
final_js = js3+"\nfunction request() {return go({"+request+"})}"
# js调用request方法返回cookie并将新的__jsl_clearance塞给session中
cookies3 = execjs.compile(final_js).call('request').split(';')[0].split('=')
session.cookies.set(cookies3[0], cookies3[1])
print(cookies3)



# 第三次请求 修改了__jsl_clearance后服务端向客户端设置新cookie的SECTOKEN
session.get(index_url)
cookies = requests.utils.dict_from_cookiejar(session.cookies)
print(cookies)

url = 'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle=&regOrg=110000'

data = {
    # 'draw': '0',
    'start': '0',
    'length': '10'
}

# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    # 'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    # 'Cookie': '__jsluid=fb0718dce34ccf53c4b94d15e9ab13d5; SECTOKEN=7178252594204902863; __jsl_clearance=1546475343.133|0|QZ7AOWMecndqD4CZG4hqoBAHtVw%3D;'
}

response = requests.post(url, cookies=cookies, data=data, headers=headers)
# response = session.post(url,data,headers)
print(response.status_code)
print(response.content.decode())
