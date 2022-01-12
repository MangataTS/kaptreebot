import json
import random
import os
import nonebot
import requests
import base64
import io
from aiocqhttp import MessageSegment
from nonebot import require
from nonebot.adapters.cqhttp import Bot, Event, Message

group_id_list=[719126877,297823886,913088980,541802647,805481638,786724450,887568508,790106567,1055277728]

scheduler = require('nonebot_plugin_apscheduler').scheduler

@scheduler.scheduled_job('cron', hour='15',minute='0', id='yincha')
async def yincha():
    (bot,) = nonebot.get_bots().values()
    for id in group_id_list:
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message='三点几嚟，做碌鸠啊做！做这么多，老板不会心疼你的,饮茶先啦！'
        )

async def get_zaobao():
    url = 'https://api.iyk0.com/60s'
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['imageUrl']
    return message
def get_today():
    url='https://api.iyk0.com/jr/'
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['surplus'])
    return message

@scheduler.scheduled_job('cron', hour='12',minute='35', id='zaobao')
async def zaobao():
    (bot,) = nonebot.get_bots().values()
    text = await get_zaobao()
    text.replace('\n', '')
    for id in group_id_list:
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message='早上好，兄弟萌☀\n━━━━━━━━\n60s读懂世界\n'+MessageSegment.image(text)
        )
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message=str(get_today())
        )


