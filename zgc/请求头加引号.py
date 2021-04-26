import re

old_headers ='''
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 186
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: gr_user_id=ab157f7c-4606-4b64-ab51-8812ef54a1dc; NTKF_T2D_CLIENTID=guestB82446A1-D56A-BA64-C164-D022AF121DA2; __utmz=12194411.1618399645.1.1.utmccn=(referral)|utmcsr=trade.5173.com|utmcct=/html/buyer/orders.aspx|utmcmd=referral; guide_loginTips=s; __utmc=12194411; Hm_lvt_6054b5813cf740e14dd8df8f5d0cb24b=1618399637,1619420551; fp=0e1a3f812cb477b339ad4c3f559a66ec; trace_5173=202104261602047023f7897e485ef391; ae7d9d7e698ddc2f_gr_last_sent_cs1=p_b4tbb4m; __utmv=12194411.p_b4tbb4m; nTalk_CACHE_DATA={uid:bq_1000_ISME9754_guestB82446A1-D56A-BA,tid:1619424178567161}; loop=0,637550504378496706; ae7d9d7e698ddc2f_gr_session_id=aacd0745-b02c-4ccc-a8a8-87fb9011108c; ae7d9d7e698ddc2f_gr_session_id_aacd0745-b02c-4ccc-a8a8-87fb9011108c=true; returnUrl=http://www.5173.com/; __utma=12194411.1397582551.1618399645.1619424128.1619427149.4; __utmb=12194411; Hm_lpvt_6054b5813cf740e14dd8df8f5d0cb24b=1619427149
Host: passport.5173.com
Origin: https://passport.5173.com
Pragma: no-cache
Referer: https://passport.5173.com/?returnUrl=http%3a%2f%2fwww.5173.com%2f
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
X-Requested-With: XMLHttpRequest

'''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in old_headers.splitlines():
    headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(headers[:-2])

