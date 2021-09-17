import requests

session = requests.session()
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'yuanrenxue.project',
    'Referer': 'http://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
session.headers = headers
url_logo = 'http://match.yuanrenxue.com/logo'
res = session.post(url_logo)
print(res, res.cookies)
url = 'http://match.yuanrenxue.com/api/match/3?page=1'
res = session.get(url=url)
data = res.json()["data"]
vl = [v['value'] for v in data]

res = session.post(url_logo)
url = 'http://match.yuanrenxue.com/api/match/3?page=2'
data = session.get(url=url).json()["data"]
vl.append([v['value'] for v in data])

session.post(url_logo)
url = 'http://match.yuanrenxue.com/api/match/3?page=3'
data = session.get(url=url).json()["data"]
vl.append([v['value'] for v in data])

session.post(url_logo)
url = 'http://match.yuanrenxue.com/api/match/3?page=4'
data = session.get(url=url).json()["data"]
vl.append([v['value'] for v in data])

session.post(url_logo)
url = 'http://match.yuanrenxue.com/api/match/3?page=5'
data = session.get(url=url).json()["data"]
vl.append([v['value'] for v in data])

print(max(vl,key=vl.count))