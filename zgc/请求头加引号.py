import re

old_headers ='''
content-type: application/json
cookie: ptui_loginuin=1014733295; RK=va4NP05bfz; ptcz=18f7f01cc903421602b4db393f3cfbeb2fc08fde11e33373820b1d1fd9c55e15; pgv_pvid=4895108636; ts_uid=702913858; ts_refer=e.qq.com/dev/index.html; adnet_uin=808020614059; adnet_uname=%E8%8B%8F%E5%B7%9E%E6%91%A9%E5%A4%9A%E5%A4%9A%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; adnet_openId=E7BB4780ACE6D9DE240C87F02ABFC82B; adnet_li=$1$fdsffdfd$dEgR7tbsbpNMmv0nhJfiJ1; adnet_sso_flag=1; adnet_sso=TGT-27188-b4LXe0Y_bngUXYeYNmuTyxKzx.yeis2dLp7wc6hvV_eAoPaaPgF.SFgQGTwUmL3r; adnet_atype=Member; pgv_info=ssid=s7697369030; ts_last=adnet.qq.com/index
origin: https://adnet.qq.com
pragma: no-cache
referer: https://adnet.qq.com/report/list
sec-fetch-mode: cors
sec-fetch-site: same-origin
sign: 20ec031148f1070b56ffffb720ad2c40
time: 1619677454486
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
x-requested-with: XMLHttpRequest
'''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in old_headers.splitlines():
    headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(headers[:-2])

