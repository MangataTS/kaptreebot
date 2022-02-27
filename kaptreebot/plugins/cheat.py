import json
import requests
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event, Message, PRIVATE



# 小思机器人
si_zhi_url = 'https://api.ownthink.com/bot'
appid = 'c8278e2921b4bc31f8974ad58dec13ba'

async def get_n(text):
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
    if event.is_tome() and int(event.get_user_id())!=event.self_id:
        mysay = event.get_message()
        mysay = await get_n(str(mysay))
        await bot.send(
            event=event,
            message=mysay
        )

