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
# url='https://chp.shadiao.app/api.php'
# headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
#     }
# t = requests.get(url,headers=headers)
#
# print(t.text)
# print('朋友圈文案+',str1)
#
# url ='https://v1.hitokoto.cn/'
# res = requests.get(url)
# c = json.loads(res.text)
# ans = c['hitokoto']+'---->'+c['from']
# print(ans)

# import json
# import urllib.request
# while 1:
#     try:
#         api_url = "http://openapi.tuling123.com/openapi/api/v2"
#         text_input = input('Mangata：')
#         if text_input == 'exit':
#             break
#         req = {
#             "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
#             "perception":  # 信息参数
#             {
#                 "inputText":  # 文本信息
#                 {
#                     "text": text_input
#                 },
#
#                 "selfInfo":  # 用户参数
#                 {
#                     "location":
#                     {
#                         "city": "南充",  # 所在城市
#                         "province": "四川",  # 省份
#                         "street": "顺庆区"  # 街道
#                     }
#                 }
#             },
#             "userInfo":
#             {
#                 "apiKey": "92f3cf04b7444a00a543e8cff93c6a13",  # 改为自己申请的key
#                 "userId": "0001"  # 用户唯一标识(随便填, 非密钥)
#             }
#         }
#         # print(req)
#         # 将字典格式的req编码为utf8
#         req = json.dumps(req).encode('utf8')
#         # print(req)
#         http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
#         response = urllib.request.urlopen(http_post)
#         response_str = response.read().decode('utf8')
#         # print(response_str)
#         response_dic = json.loads(response_str)
#         # print(response_dic)
#         intent_code = response_dic['intent']['code']
#         results_text = response_dic['results'][0]['values']['text']
#         print('kaptree：', results_text)
#         # print('code：' + str(intent_code))
#     except KeyError:
#         print('出错啦~~, 下次别问这样的问题了')
