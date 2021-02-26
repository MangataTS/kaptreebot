import json
import requests
from nonebot import on_message,on_command
from nonebot.adapters.cqhttp import Bot, Event, Message, PRIVATE

#图灵机器人
# def get_n(text_input:str):
#     try:
#         api_url = "http://openapi.tuling123.com/openapi/api/v2"
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
#         if str(results_text) == '请求次数超限制!':
#             return '今天的智能对话次数用完了呢QAQ'
#         return str(results_text)
#         # print('code：' + str(intent_code))
#     except KeyError:
#         if KeyError == '4003':
#             return '今天的智能对话次数用完了呢QAQ,请输入help查看其他玩法叭'
#         else:
#             return '这个问题好头疼呀，问点别的叭'

# 小思机器人
si_zhi_url = 'https://api.ownthink.com/bot'
appid = 'c8278e2921b4bc31f8974ad58dec13ba'

def get_n(text):
    try:
        data = {
            "spoken": text,
            "appid": appid,
            "userid": "HRPVyRSl"
        }
        r = requests.post(si_zhi_url, data=json.dumps(data))
        result = json.loads(r.content)
        message = result['data']['info']['text']
        if 'heuristic' in result['data']['info'] and result['data']['info']['heuristic']:
            for item in result['data']['info']['heuristic']:
                message += ',  ' + item
        print(message)
        return message
    except KeyError:
        return '这个问题好头疼呀，问点别的叭'


tuling = on_message(priority=5) # permission= PRIVATE
@tuling.handle()
async def cheatt_(bot:Bot,event:Event):
    if event.is_tome():
        print("YES")
    if event.is_tome() and event.user_id!=event.self_id:
        mysay = event.get_message()
        mysay = get_n(str(mysay))
        await bot.send(
            event=event,
            message=mysay
        )

