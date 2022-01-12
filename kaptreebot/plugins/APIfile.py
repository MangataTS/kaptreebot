from requests_html import HTMLSession
import requests
from nonebot import on_command
from nonebot import on_keyword,on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, Message
import random
from aiocqhttp import MessageSegment
import json
from nonebot.adapters.cqhttp import message

async def get_biao(text:str):
    url = ('https://api.iyk0.com/sbqb/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    l = result['sum']
    k = random.randint(0, l)
    message = result['data_img'][k]['img']
    print(message)
    return message

BQB = on_command("表情包", priority=2)
@BQB.handle()
async def BQB_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["biao"] = args  # 如果用户发送了参数则直接赋值


@BQB.got("biao", prompt="你想查询神马表情包(@_@)...")
async def handle_biao(bot: Bot, event: Event, state: dict):
    biao = state["biao"]
    biaoqingbao = await get_biao(biao)
    await bot.send(
        event = event,
        message=MessageSegment.image(biaoqingbao)
    )

async def get_wangzhe(text:str):
    url = ('https://api.iyk0.com/wzcz/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['img']
    print(message)
    return message

# 王者荣耀出装
WZRY = on_command("王者荣耀", priority=2)
@WZRY.handle()
async def WZ_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["king"] = args  # 如果用户发送了参数则直接赋值


@WZRY.got("king", prompt="你想查询什么英雄(@_@)...")
async def handle_WZ(bot: Bot, event: Event, state: dict):
    king = state["king"]
    wangzhe = await get_wangzhe(king)
    await bot.send(
        event = event,
        message=MessageSegment.image(wangzhe)
    )

async def get_DSP():
    url = 'https://api.iyk0.com/dsp/?type=网红'
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['url']
    print(message)
    return message

# 短视频
DSP = on_command("短视频", priority=2)
@DSP.handle()
async def WZ_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment(type_='video',
               data=({
                   'file': str(await get_DSP())
               }))
        )

# 抽签小游戏

async def get_chou(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抽签&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

CouQ = on_command("抽签", priority=2)
@CouQ.handle()
async def chouqian_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_chou(str(Event.get_user_id))),
            at_sedner=True
        )
async def get_pao(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抛杯&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

PB = on_command("抛杯", priority=2)
@PB.handle()
async def paobei_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_pao(str(Event.get_user_id))),
            at_sedner=True
        )
async def get_jie(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=解签&n='+qq
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['title']+'\n'+result['desc'])
    print(message)
    return message

PB = on_command("解签", priority=2)
@PB.handle()
async def paobei_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(await get_jie(str(Event.get_user_id))),
            at_sedner=True
        )
# 语音转换
async def get_yuying(text:str):
    url = ('https://api.iyk0.com/yy/?msg='+text)
    r = requests.get(url)
    message = r.text
    print(message)
    return message


YYZH = on_command("语音转换", priority=2)
@YYZH.handle()
async def YY_(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["yuying"] = args  # 如果用户发送了参数则直接赋值


@YYZH.got("yuying", prompt="你想转换什么")
async def handle_YY(bot: Bot, event: Event, state: dict):
    yuying = state["yuying"]
    huan = str(get_yuying(yuying))
    huan = huan.replace('\n', '')
    await bot.send(
        event=event,
        message=MessageSegment(type_='record',data=({'file': huan}))
    )