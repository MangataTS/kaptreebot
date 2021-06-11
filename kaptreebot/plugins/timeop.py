import json
import random
import os
import nonebot
import requests
import base64
import io
from aiocqhttp import MessageSegment
from nonebot import require

group_id_list=[719126877,297823886,913088980,541802647,805481638,786724450,887568508,790106567]

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
#大佬大佬，晚饭晚饭(偷吃。味道很棒喵！

@scheduler.scheduled_job('cron', hour='18',minute='0', id='wanfan')
async def wanfan():
    (bot,) = nonebot.get_bots().values()
    for id in group_id_list:
        await bot.send_msg(
            message_type="group",
            group_id=int(id),
            message='大佬大佬，晚饭晚饭(偷吃.味道很棒喵！'
        )


