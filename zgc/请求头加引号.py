import re

old_headers ='''
userid: 15806204095
pwd: 74ce2ba17b2c218246e778fb5e895c95
isAuto: 1
backurl: http://www.zol.com.cn/
tmallBtn: 0
activeBtn: 0
headPicid: 0

'''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in old_headers.splitlines():
    headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(headers[:-2])

