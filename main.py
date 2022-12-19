# encoding=utf8

import requests
import json

cookies = {
    'lang': 'zh-cn',
    'uid': '755899',
    'email': '110muzicul110%40gmail.com',
    'key': '75fe857f6fee3f6118b62bd1d508f2d80a632ce155e6d',
    'ip': '9b90675e640e5f5a99aa5d062ec52706',
    'expire_in': '1671454410',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Referer': 'https://ikuuu.co/user',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://ikuuu.co',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
}


def sign_in_iku():
    try:
        response = requests.post('https://ikuuu.co/user/checkin', cookies=cookies, headers=headers,
                                            proxies={'http': f'http://127.0.0.1:11223',
                                                     'https': f'http://127.0.0.1:11223'})
        text = json.loads(response.text)
        if text['ret'] == 0:
            serverChan(text['msg'])
        if text['ret'] == 1:
            serverChan(text['msg'])
    except Exception as e:
        serverChan('流量签到服务器错误：'+str(e))


def serverChan(content):
        title = '签到结果'
        sendkey = ''
        assert type(sendkey) == str, "Wrong type for serverChan token." 
        content = content.replace("\n","\n\n")
        payload = {
            "title": title,
            "desp": content, 
        }
        resp = requests.post(f"https://sctapi.ftqq.com/{sendkey}.send", data=payload)
        resp_json = resp.json()
        if resp_json["code"] == 0:
            print(f"【ServerChan】Send message to ServerChan successfully.")
        if resp_json["code"] != 0:
            print(f"【ServerChan】【Send Message Response】{resp.text}")
            return -1
        return 0
