import time
import execjs
import requests
def get_page(page_num,parameters):
    url = 'http://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(page_num,parameters)
    headers = {
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/1',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'qpfccr=true; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1607556997,1607557857; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1607557857; no-alert=true'
    }
    response = requests.get(url=url,headers=headers)
    return response.json()

def calculate_m_value():
    with open(r'1.js',encoding='utf-8',mode='r') as f:
        JsData = f.read()
    psd = execjs.compile(JsData).call('request')
    psd = psd.replace('丨','%E4%B8%A8')
    print('this request parameters is :',psd)
    return psd

if __name__ == '__main__':
    sum_num = 0
    index_num = 0
    for page_num in range(1,6):
        res = get_page(page_num,calculate_m_value())
        data = [__['value'] for __ in res['data']]
        print(data)
        sum_num+=sum(data)
        index_num += len(data)
        time.sleep(1)

    average = sum_num/index_num
    print('the answer is :',average)