import requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event
import random
from nonebot.adapters.onebot.v11 import MessageSegment
import json

from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

def get_biao(text:str):
    url = ('https://api.iyk0.com/sbqb/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    l = result['sum']
    k = random.randint(0, l)
    message = result['data_img'][k]['img']
    print(message)
    return message

BQB = on_command("表情包", rule=to_me(),priority=2,block=True)

@BQB.handle()
async def BQB_(matcher: Matcher, args: Message = CommandArg()):
        plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if plain_text:
            matcher.set_arg("biao", args)  # 如果用户发送了参数则直接赋值



@BQB.got("biao", prompt="你想查询神马表情包(@_@)...")
async def handle_biao(biao: Message = Arg(), biao_name: str = ArgPlainText("biao")):
    print(biao_name)
    biaoqingbao = get_biao(biao_name)
    await BQB.send(MessageSegment.image(biaoqingbao))

def get_wangzhe(text:str):
    url = ('https://api.iyk0.com/wzcz/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['img']
    print(message)
    return message

# 王者荣耀出装
WZRY = on_command("王者荣耀", priority=2,block=True)
@WZRY.handle()
async def WZ_(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("king", args)  # 如果用户发送了参数则直接赋值


@WZRY.got("king", prompt="你想查询什么英雄(@_@)...")
async def handle_WZ(king: Message = Arg(), king_name: str = ArgPlainText("king")):
    wangzhe = get_wangzhe(king_name)
    await WZRY.send(MessageSegment.image(wangzhe))

def get_DSP():
    url = 'https://api.iyk0.com/dsp/?type=网红'
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['url']
    return message

# # 短视频
# DSP = on_command("短视频", priority=2,block=True)
# @DSP.handle()
# async def DSP_(bot: Bot, event: Event):
#     if int(event.get_user_id()) != event.self_id:
#         url=get_DSP()
#         print(url)
#         await DSP.send(MessageSegment.video(url))
#         #(type_='video',data=({'file': str(get_DSP())})

# 抽签小游戏

def get_chou(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抽签&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

CouQ = on_command("抽签", priority=2,block=True)
@CouQ.handle()
async def chouqian_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_chou(str(Event.get_user_id))),
            at_sedner=True
        )
def get_pao(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=抛杯&n='+qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message

PB = on_command("抛杯", priority=2,block=True)
@PB.handle()
async def paobei_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_pao(str(Event.get_user_id))),
            at_sedner=True
        )
def get_jie(qq:str):
    url = 'https://api.iyk0.com/gdlq/?msg=解签&n='+qq
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['title']+'\n'+result['desc'])
    print(message)
    return message

JQ = on_command("解签", priority=2,block=True)
@JQ.handle()
async def JQ_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_jie(str(Event.get_user_id))),
            at_sedner=True
        )
# 语音转换
def get_yuying(text:str):
    url = ('https://api.iyk0.com/yy/?msg='+text)
    r = requests.get(url)
    message = r.text
    print(message)
    return message


YYZH = on_command("语音转换", priority=2,block=True)
@YYZH.handle()
async def YY_(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("yuying", args)  # 如果用户发送了参数则直接赋值


@YYZH.got("yuying", prompt="你想转换什么")
async def handle_YY(yuying: Message = Arg(), yuying_name: str = ArgPlainText("yuying")):
    huan = str(get_yuying(yuying_name))
    huan = huan.replace('\n', '')
    print("转换内容: ",huan)
    await YYZH.send(MessageSegment.record(huan))