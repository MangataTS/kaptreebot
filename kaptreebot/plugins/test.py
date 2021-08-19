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

# si_zhi_url = 'https://api.ownthink.com/bot'
# appid = 'c8278e2921b4bc31f8974ad58dec13ba'
#
# def get_n(text):
#     try:
#         data = {
#             "spoken": text,
#             "appid": appid,
#             "userid": "HRPVyRSl"
#         }
#         r = requests.post(si_zhi_url, data)
#         result = json.loads(r.content)
#         message = result['data']['info']['text']
#         print(message)
#         return message
#     except KeyError:
#         print("error")
#         return '这个问题好头疼呀，问点别的叭'
# get_n("你喜欢什么")

def get_biao(text):
    url = ('https://api.iyk0.com/sbqb/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    len = result['sum']
    print(len)
    message = result['data_img'][0]['img']
    print(message)
    return message
get_biao('好家伙')

# def get_zaobao():
#     url = 'https://api.iyk0.com/60s'
#     r = requests.get(url)
#     result = json.loads(r.content)
#     message = result['imageUrl']
#     return message
# print(get_zaobao())
def get_yuying(text:str):
    url = ('https://api.iyk0.com/yy/?msg='+text)
    r = requests.get(url)
    message = r.text
    print(message)
get_yuying("好家伙")