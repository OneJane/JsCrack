import requests
import execjs

account = "***"
password = "***"


def get_pwd():
    with open("fang.js", "r") as f:
        js_code = f.read()
    results = execjs.compile(js_code).call("getpwd", password)
    return results


def login():
    url = 'https://passport.fang.com/login.api'
    pwd = get_pwd()
    data = {
        'uid': account,
        'pwd': pwd,
        'Service': 'soufun-passport-web',
        'AutoLogin': '1',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'passport.fang.com',
        'Origin': 'https://passport.fang.com',
        'Pragma': 'no-cache',
        'Referer': 'https://passport.fang.com/?backurl=https%3A%2F%2Fsuzhou.fang.com%2F',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    response = requests.post(url, data, headers=headers)
    print(response.text)


if __name__ == '__main__':
    login()
