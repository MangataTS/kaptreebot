from ctypes import Union

from nonebot.permission import SUPERUSER
from requests_html import HTMLSession
import requests
from nonebot import on_command
from nonebot import on_keyword,on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, Message
import random
from aiocqhttp import MessageSegment
import os

kiss=['么么哒','不要这样嘛!','你好讨厌哦!','你好坏哦，欺负人家，哼！','不要酱紫嘛','一天没和你聊天，就觉得哪里不对劲！','快亲亲人家啦!!','不理你了，真讨厌。','人家不要了啦!','你今天有没有想念人家呀!',
      '别这样啦，人家是个女孩子嘛!','(✿◡‿◡)','(*/ω＼*)','つ﹏⊂','ヾ(≧O≦)〃嗷~','(>▽<)，好呀','恶心心','mu--a','可以教我写代码吗','记得AK比赛哦','能AK比赛吗？']

# 图片资源库,但是貌似没啥用了，因为图片爬虫写好了
setu=['https://i.im5i.com/2021/02/11/hPbND.jpg','http://p4.qhimg.com/bdm/480_296_0/t0143a132026482b568.jpg','http://p2.qhimg.com/bdm/480_296_0/t010c82b9ebddaf84bb.jpg',
      'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2097012350,544381752&fm=26&gp=0.jpg','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3876952931,2872354563&fm=26&gp=0.jpg',
      'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1184459843,998082392&fm=26&gp=0.jpg','https://i-ogp.pximg.net/c/w1200_q80_a2_g1_u1_cr0:0.094:1:0.427/img-master/img/2020/10/09/17/00/00/84899204_p0_master1200.jpg',
      'http://pic1.win4000.com/wallpaper/d/555301fee25be.jpg','http://pic1.win4000.com/wallpaper/f/5485742a3fc52.jpg','http://pic1.win4000.com/wallpaper/f/5485742cebe37.jpg','http://pic1.win4000.com/wallpaper/f/5485742f9f324.jpg',
      'http://pic1.win4000.com/wallpaper/f/5485743258aa2.jpg','http://pic1.win4000.com/wallpaper/f/548574354dae7.jpg','http://pic1.win4000.com/wallpaper/f/5485743e00c7c.jpg','http://pic1.win4000.com/wallpaper/f/54857440e681b.jpg',
      'http://pic1.win4000.com/wallpaper/5/548ea9fa1cc3c.jpg','http://pic1.win4000.com/wallpaper/5/548ea9fe13075.jpg','http://pic1.win4000.com/wallpaper/f/54743eba914e0.jpg','http://pic1.win4000.com/wallpaper/f/54743ebdb4791.jpg',
      'http://pic1.win4000.com/wallpaper/b/54743d878ab75.jpg','http://pic1.win4000.com/wallpaper/b/54743d8e5e080.jpg','http://pic1.win4000.com/wallpaper/b/54743d912ac40.jpg','http://pic1.win4000.com/wallpaper/4/548fc1461345c.jpg',
      'http://pic1.win4000.com/wallpaper/4/548fc14f27ff6.jpg','https://pic3.zhimg.com/80/v2-bc8fb0f787fe3e84bf51f304a20614da_720w.jpg','https://pic3.zhimg.com/80/v2-b7b9156ee6ae8c80c8e23b15069f50fa_720w.jpg',
      'https://pic2.zhimg.com/80/v2-cf4c5e853055f4fa7bcadbb1aaece911_720w.jpg','https://pic1.zhimg.com/80/v2-dcd1558fb089fb765ffa3d223d30680e_720w.jpg','https://pic2.zhimg.com/80/v2-5a90b3f0446c0a77d67a9b69c20fe6cd_720w.jpg',
      'https://pic4.zhimg.com/80/v2-759f11bc6819aeb4f9d655c7fe8f0266_720w.jpg','https://i.im5i.com/2021/02/11/hPToq.jpg','https://i.im5i.com/2021/02/11/hPjJt.jpg','https://i.im5i.com/2021/02/11/hPWMm.jpg','https://i.im5i.com/2021/02/11/hP2ds.jpg',
      'https://i.im5i.com/2021/02/11/hP9XQ.jpg','https://i.im5i.com/2021/02/11/hPR03.jpg','https://i.im5i.com/2021/02/11/hPnSy.jpg','https://i.im5i.com/2021/02/11/hPotO.md.jpg','https://i.im5i.com/2021/02/11/hP3xR.jpg',
      'https://i.im5i.com/2021/02/11/hPZwd.png','https://i.im5i.com/2021/02/11/hPiJ4.jpg','https://i.im5i.com/2021/02/11/hPmoW.jpg','https://i.im5i.com/2021/02/11/hPxOG.png','https://i.im5i.com/2021/02/11/hPAdz.jpg',
      'https://i.im5i.com/2021/02/11/hPLX5.md.jpg','https://i.im5i.com/2021/02/11/hPeD6.md.png','https://i.im5i.com/2021/02/11/hP0S8.jpg','https://i.im5i.com/2021/02/11/hPDuU.png','https://i.im5i.com/2021/02/11/hPa8w.png',
      'https://i.im5i.com/2021/02/11/hPpwZ.md.jpg','https://i.im5i.com/2021/02/11/hP7cJ.md.png','https://i.im5i.com/2021/02/11/hPM31.jpg','https://i.im5i.com/2021/02/11/hPOOn.jpg','https://i.im5i.com/2021/02/11/hV1fl.png',
      'https://i.im5i.com/2021/02/11/hVFX7.jpg','https://i.im5i.com/2021/02/11/hVQD2.jpg','https://i.im5i.com/2021/02/11/hVwgP.md.jpg','https://i.im5i.com/2021/02/11/hVCuD.md.jpg','https://i.im5i.com/2021/02/11/hVq8j.png',
      'https://i.im5i.com/2021/02/11/hV6CS.jpg','https://i.im5i.com/2021/02/11/hVNcL.jpg','https://i.im5i.com/2021/02/11/hVS3t.md.jpg','https://i.im5i.com/2021/02/11/hVgkq.png','https://i.im5i.com/2021/02/11/hVKfm.jpg',
      'https://i.im5i.com/2021/02/11/hVP2s.png','https://i.im5i.com/2021/02/11/hVVaQ.jpg','https://i.im5i.com/2021/02/11/hVfg3.jpg','https://i.im5i.com/2021/02/11/hVl5y.md.png','https://i.im5i.com/2021/02/11/hVr8O.jpg',
      'https://i.im5i.com/2021/01/21/Qf8y1.jpg','https://i.im5i.com/2021/01/21/QfxFJ.jpg','https://i.im5i.com/2021/01/21/QfiZZ.jpg','https://i.im5i.com/2021/01/21/QfZUw.jpg','https://i.im5i.com/2021/01/21/QfIvU.jpg','https://i.im5i.com/2021/01/21/QfoL8.jpg',
       'https://i.im5i.com/2021/01/21/QfYK5.jpg','https://i.im5i.com/2021/01/21/Qf94z.jpg','https://i.im5i.com/2021/01/21/Qf2RG.jpg','https://i.im5i.com/2021/01/21/QfXrW.jpg','https://i.im5i.com/2021/01/21/QfW14.jpg','https://i.im5i.com/2021/01/21/QfjZd.jpg',
       'https://i.im5i.com/2021/01/21/QfHER.jpg','https://i.im5i.com/2021/01/21/Qf5qO.jpg','https://i.im5i.com/2021/01/21/QftLy.jpg','https://i.im5i.com/2021/01/21/QfbH3.jpg','https://i.im5i.com/2021/01/21/QfUKQ.jpg','https://i.im5i.com/2021/01/21/Qfs4s.jpg',
       'https://i.im5i.com/2021/01/21/Qfc9m.jpg','https://i.im5i.com/2021/01/21/QfJrq.jpg','https://i.im5i.com/2021/01/21/QfB1t.jpg','https://i.im5i.com/2021/01/21/QfrIL.jpg','https://i.im5i.com/2021/01/21/QflES.jpg','https://i.im5i.com/2021/01/21/Qffqj.jpg',
        'https://i.im5i.com/2021/01/21/QfVAD.jpg','https://i.im5i.com/2021/01/21/QfPHP.md.jpg','https://i.im5i.com/2021/01/21/QfKG2.jpg','https://i.im5i.com/2021/01/21/Qfga7.jpg','https://i.im5i.com/2021/01/21/QfS9l.jpg','https://i.im5i.com/2021/01/21/QfNln.jpg',
        'https://i.im5i.com/2021/01/21/Qf611.jpg','https://i.im5i.com/2021/01/21/QdDsd.md.jpg','https://i.im5i.com/2021/01/21/QdAg3.md.jpg','https://i.im5i.com/2021/01/21/Qde8O.md.jpg','https://i.im5i.com/2021/01/21/QdxaQ.md.jpg','https://i.im5i.com/2021/01/21/Qdm2s.jpg',
        'https://ss.im5i.com/2020/10/23/46ead76526b520ec98397b493c889642.jpg','https://i.im5i.com/2021/01/26/QxnWZ.jpg','https://i.im5i.com/2021/01/26/Qxo0J.jpg','https://i.im5i.com/2021/01/26/QxYdw.jpg','https://i.im5i.com/2021/01/26/QxIS1.jpg',
          'https://i.im5i.com/2021/01/26/QxZtn.jpg','https://i.im5i.com/2021/01/26/Qxixl.jpg','https://i.im5i.com/2021/01/26/Qxxh7.jpg','https://i.im5i.com/2021/01/28/QD3lz.jpg','https://i.im5i.com/2021/01/28/QDmG8.jpg','https://i.im5i.com/2021/01/28/QDI95.jpg','https://i.im5i.com/2021/01/30/Qajyn.jpg']

music_=['http://music.163.com/song/media/outer/url?id=1817935489.mp3','http://music.163.com/song/media/outer/url?id=1816835031.mp3','http://music.163.com/song/media/outer/url?id=1813913037.mp3',
        'http://music.163.com/song/media/outer/url?id=1813389565.mp3','http://music.163.com/song/media/outer/url?id=452986458.mp3',]

def get_setu():
    url='https://api.ixiaowai.cn/api/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c

def get_mc():
    url='https://api.ixiaowai.cn/mcapi/mcapi.php'
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

# 社会语录
def get_shehui():
    url='https://du.liuzhijin.cn/yulu.php'
    session = HTMLSession()
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    r = session.get(url,headers=headers)
    sel ='#text'
    s = r.html.find(sel)
    str1 = s[0].text
    print('社会语录+',str1)
    return str1

explain = on_command("我要亲亲",aliases={'我要抱抱'} ,priority=2)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        k = (random.randint(0,10000)+random.randint(0,10000))%len(kiss)
        s = kiss[k]
        print('kiss总数目',len(kiss),'我要抱抱指令输出:',s)
        await bot.send(
            event=event,
            message=s,
            at_sender=True
        )

st = on_keyword({'setu','涩图','色图','每日一图'}, priority=2)
@st.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_setu()),
        )

mc = on_keyword(['mc表情包','MC酱','Mc酱','mC酱',"mc酱"],priority=2)
@mc.handle()
async def mcpo(bot: Bot,event: Event,state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_mc()),
            at_sender=True
        )

dudu = on_keyword(['毒鸡汤'],priority=2)
@dudu.handle()
async def getdu_(bot:Bot,event:Event,state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_dujit())
        await bot.send(
            event=event,
            message= str1,
            at_sedner=True
        )

shehui = on_keyword(['社会语录'],priority=2)
@shehui.handle()
async def shehui_(bot:Bot,event:Event,state: dict):
    if event.get_user_id != str(event.self_id):
        str1 = str(get_shehui())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )

ac = on_keyword(['主人'],priority=2)
@ac.handle()
async def ACAC(bot:Bot,event: Event,state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message='我是大家的哦，请大家爱护我，不要对我说一些奇怪的话'
        )

newyear = on_command("新年快乐",priority=2)
@newyear.handle()
async def resp(bot:Bot,event: Event,state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message='新年快乐鸭，（づ￣3￣）づ╭❤～',
            at_sender=True
        )

help = on_command("查看说明",aliases={'help','帮助','使用说明'},priority=2)
@help.handle()
async def help_(bot:Bot,event: Event,state: dict):
    await bot.send(
        event=event,
        message='1.每日一句 eg:/每日一句\n'
                '2.天气查询 eg:/天气 成都\n'
                '3.翻译 eg:/翻译 cat\n'
                '4.戳一戳 eg:手机戳我头像\n'
                '5.精彩图片 eg:关键词匹配("/每日一图"，"/mc酱")\n'
                '6.我要抱抱 eg 我要抱抱\n'
                '7.新年快乐\n'
                '8.情感语录 && /毒鸡汤eg:情感语录/毒鸡汤\n'
                '9.社会语录 eg:关键词匹配(“/社会语录”)\n'
                '10.注意私聊的时候可以不加前缀/，群聊的时候可以@我或者/\n'
                '11. To be continue……'
    )
