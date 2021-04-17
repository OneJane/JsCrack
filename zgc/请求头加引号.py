import re

old_headers ='''
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Length: 341
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Cookie: JSESSIONID=DD188088D4E4EAC0098C9CCBCC32E52F; Hm_lvt_62d04228e1f84e012c1d9c0227f722c3=1618618136; Hm_lpvt_62d04228e1f84e012c1d9c0227f722c3=1618618136
Host: www.jycinema.com
Origin: http://www.jycinema.com
Proxy-Connection: keep-alive
Referer: http://www.jycinema.com/wap/
token
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36

'''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in old_headers.splitlines():
    headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(headers[:-2])

