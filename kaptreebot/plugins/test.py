#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from requests_html import HTMLSession
url ='https://v1.hitokoto.cn/?c=j&c=k'
res = requests.get(url)
c = json.loads(res.text)
ans = c['hitokoto']+'---->'+c['from']
print(ans)

si_zhi_url = 'https://api.ownthink.com/bot'
appid = 'c8278e2921b4bc31f8974ad58dec13ba'

def get_n(text):
    try:
        data = {
            "spoken": text,
            "appid": appid,
            "userid": "HRPVyRSl"
        }
        r = requests.post(si_zhi_url, data)
        result = json.loads(r.content)
        message = result['data']['info']['text']
        print(message)
        return message
    except KeyError:
        print("error")
        return '这个问题好头疼呀，问点别的叭'
get_n("你喜欢什么")