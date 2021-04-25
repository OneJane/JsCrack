import hashlib
import json
import re
import time
from jsonpath import jsonpath
import requests

APPKEY = '12574478'
DATA = '{"videoId": "%s","from":"detail"}' % "301079547561"
URL = 'https://h5api.m.taobao.com/h5/mtop.taobao.cloudvideo.video.queryforh5/1.0/'
params = {'jsv': '2.4.11', 'appKey': APPKEY, 't': int(time.time() * 1000),
          'sign': 'FAKE_SIGN_WITH_ANYTHING', 'api': 'mtop.wdetail.getItemDescx', 'callback': 'mtopjsonp1','v': '4.9',
          'type': 'jsonp', 'dataType': 'jsonp',
          'data': DATA}
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 ' + \
                  '(KHTML, like Gecko) Version/9.0 Mobile/13G35 Safari/601.1',
}
images = []
# get token in first request
r1 = requests.get(URL, params=params, headers=headers)
token_with_time = r1.cookies.get('_m_h5_tk')
token = token_with_time.split('_')[0]
enc_token = r1.cookies.get('_m_h5_tk_enc')
# get results in second request
t2 = str(int(time.time() * 1000))
c = '&'.join([token, t2, APPKEY, DATA])
m = hashlib.md5()
m.update(c.encode('utf-8'))
params.update({'t': t2, 'sign': m.hexdigest()})
cookies = {'_m_h5_tk': token_with_time, '_m_h5_tk_enc': enc_token}
r2 = requests.get(URL, params=params, headers=headers, cookies=cookies)
results=json.loads(re.match(r' mtopjsonp1\((.*?)\)', r2.text).group(1))
video_url = jsonpath(results, '$..video_url')[1]
print(video_url)
