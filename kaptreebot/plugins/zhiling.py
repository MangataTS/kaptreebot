import os
from requests_html import HTMLSession
import requests
from nonebot import on_command
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event
import random
from nonebot.adapters.onebot.v11 import MessageSegment
import json
from nonebot.typing import T_State

kiss=['么么哒','不要这样嘛!','你好讨厌哦!','你好坏哦，欺负人家，哼！','不要酱紫嘛','一天没和你聊天，就觉得哪里不对劲！','快亲亲人家啦!!','不理你了，真讨厌。','人家不要了啦!','你今天有没有想念人家呀!',
      '别这样啦，人家是个女孩子嘛!','(✿◡‿◡)','(*/ω＼*)','つ﹏⊂','ヾ(≧O≦)〃嗷~','(>▽<)，好呀','恶心心','mu--a','可以教我写代码吗','记得AK比赛哦','能AK比赛吗？']

music_=['http://music.163.com/song/media/outer/url?id=1817935489.mp3','http://music.163.com/song/media/outer/url?id=1816835031.mp3','http://music.163.com/song/media/outer/url?id=1813913037.mp3',
        'http://music.163.com/song/media/outer/url?id=1813389565.mp3','http://music.163.com/song/media/outer/url?id=452986458.mp3',]

# 获取图片
def get_setu():
    url='https://api.iyk0.com/ecy/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c


# MC酱的表情包
def get_mc():
    url='https://api.ixiaowai.cn/mcapi/mcapi.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c


# 有一定概率刷出R18的图https://api.iyk0.com/mtyh
def get_R18():
    url='https://api.iyk0.com/mty'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c




# 毒鸡汤语录
def get_dujit():
    url='https://du.liuzhijin.cn/'
    session = HTMLSession()
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    r = session.get(url,headers=headers)
    sel ='#text'
    s = r.html.find(sel)
    str1 = s[0].text
    print('毒鸡汤+',str1)
    return str1


# 朋友圈文案
def get_wenan():
    url='https://pyq.shadiao.app/api.php'
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    t = requests.get(url,headers=headers)
    c = t.text
    print('朋友圈文案',c)
    return c


# 彩虹屁
def get_caihongpi():
    url='https://chp.shadiao.app/api.php'
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    t = requests.get(url,headers=headers)
    c = t.text
    print('彩红屁',c)
    return c


# 网易语录
def get_wangyi():
    url ='https://v1.hitokoto.cn/?c=j&c=k'
    res = requests.get(url)
    c = json.loads(res.text)
    ans = c['hitokoto']+'---->'+c['from']
    print(ans)
    return ans


explain = on_command(cmd="我要亲亲",aliases={'我要抱抱'},priority=2,block=True)
@explain.handle()
async def explainsend(bot: Bot, event: Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            k = (random.randint(0,10000)+random.randint(0,10000))%len(kiss)
            s = str(kiss[k])
            print('kiss总数目',len(kiss),'我要抱抱指令输出:',s)
            await bot.send(
                event=event,
                message=s,
                at_sender=True,
            )
    except Exception as e:
        await explain.send("我要亲亲插件出现故障，请联系Mangata")


st = on_keyword(keywords={'每日一图'}, priority=2,block=True)
@st.handle()
async def st_(bot: Bot, event: Event):
    try:
        url=str(get_setu())
        if int(event.get_user_id()) != event.self_id:
            await st.send(MessageSegment.image(file=str(url)))
    except Exception as e:
        await st.send("每日一图插件出现故障，请联系Mangata")

#'setu','涩图','色图',

R18 = on_keyword(keywords={'R18','r18'}, priority=2,block=True)
@R18.handle()
async def R18_(bot: Bot, event: Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            await R18.send(MessageSegment.image(file=str(get_R18())))
    except Exception as e:
        await R18.send("R18插件出现故障，请联系Mangata")


mc = on_keyword(['mc表情包','MC酱','Mc酱','mC酱',"mc酱"],priority=2,block=True)
@mc.handle()
async def mcpo(bot: Bot,event: Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            await bot.send(
                event=event,
                message=MessageSegment.image(get_mc()),
                at_sender=True
            )
    except Exception as e:
        await mc.send("mc表情包插件出现故障，请联系Mangata")



dudu = on_keyword(['毒鸡汤'],priority=2,block=True)
@dudu.handle()
async def getdu_(bot:Bot,event:Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            str1 = str(get_dujit())
            await bot.send(
                event=event,
                message= str1,
                at_sedner=True
            )
    except Exception as e:
        await dudu.send("毒鸡汤插件出现故障，请联系Mangata")


wangyi = on_command('开始网抑',priority=2,block=True)
@wangyi.handle()
async def wangyi_(bot:Bot,event:Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            str1 = str(get_wangyi())
            await bot.send(
                event=event,
                message= str1,
                at_sedner=True
            )
    except Exception as e:
        await wangyi.send("开始网抑插件出现故障，请联系Mangata")

caihong = on_command(cmd='彩虹屁',priority=2,block=True)
@caihong.handle()
async def caihong_(bot:Bot,event:Event):
    try:
        str1 = str(get_caihongpi())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )
    except Exception as e:
        await caihong.send("彩虹屁插件出现故障，请联系Mangata")

pyqwenan= on_command('朋友圈文案',priority=2,block=True)
@pyqwenan.handle()
async def pyqwenan_(bot:Bot,event:Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            str1 = str(get_wenan())
            await bot.send(
                event=event,
                message= str1,
                at_sedner=True
            )
    except Exception as e:
        await pyqwenan.send("朋友圈文案插件出现故障，请联系Mangata")


help = on_command("查看说明",aliases={'help','帮助','使用说明'},priority=2,block=True)
@help.handle()
async def help_(bot:Bot,event: Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            path_ = os.getcwd()
            path_ = path_ + '\help.png'
            mypath = 'file:///' + path_
            print(mypath)
            await bot.send(
                event=event,
                message=MessageSegment.image(mypath)
            )
    except Exception as e:
        await help.send("查看说明插件出现故障，请联系Mangata")
zhibo= on_command('$直播',priority=2,block=True)
@zhibo.handle()
async def zhibo_(bot:Bot,event:Event):
    try:
        print(event.get_user_id())
        print(event.self_id)
        if int(event.get_user_id()) != event.self_id:
            str1 = '主人，您订阅的直播间开播辣，快来看看叭\n地址:https://live.bilibili.com/22864638'
            await bot.send(event=event,group_id = 913088980,message=str1)
    except Exception as e:
        await zhibo.send("直播发送插件出现故障，请联系Mangata")

# test = on_command('test',priority=2)
# @test.handle()
# async def test_(bot:Bot,event:Event,state: dict = T_State):
#     url = 'https://api.iyk0.com/60s'
#     r = requests.get(url)
#     result = json.loads(r.content)
#     message = result['imageUrl']
#     print(message)
#     await bot.send(
#         event=event,
#         message=MessageSegment.image(message)
#     )