import requests
import execjs
import time

def get_page(page_num,param):
    url = "http://match.yuanrenxue.com/api/match/2?page={}".format(page_num)
    headers = {
        'Host': 'match.yuanrenxue.com',
        'Referer':'http://match.yuanrenxue.com/match/2',
        'User-Agent':'yuanrenxue.project',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie': param
    }
    resonse = requests.get(url=url,headers=headers)
    return resonse.json()
def calculate_m_value():
    with open(r'2.js',encoding='utf-8',mode='r') as f:
        JsData = f.read()
    psd = execjs.compile(JsData).call('request')
    psd = psd.replace('丨','%E4%B8%A8')
    print('this request parameters is :',psd)
    return psd

if __name__ == '__main__':
    sum_num = 0
    for page_num in range(1,6):
        res = get_page(page_num,calculate_m_value())
        data = [__['value'] for __ in res['data']]
        print(data)
        sum_num+=sum(data)
        time.sleep(1)

    print('the answer is :',sum_num)