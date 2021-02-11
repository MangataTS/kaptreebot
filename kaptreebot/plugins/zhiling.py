from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import random
from aiocqhttp import MessageSegment

kiss=['么么哒','不要这样嘛!','你好讨厌哦!','你好坏哦，欺负人家，哼！','不要酱紫嘛','一天没和你聊天，就觉得哪里不对劲！','快亲亲人家啦!!','不理你了，真讨厌。','人家不要了啦!','你今天有没有想念人家呀!',
      '别这样啦，人家是个女孩子嘛!','(✿◡‿◡)','(*/ω＼*)','つ﹏⊂','ヾ(≧O≦)〃嗷~','(>▽<)，好呀']

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
      'https://i.im5i.com/2021/02/11/hVP2s.png','https://i.im5i.com/2021/02/11/hVVaQ.jpg','https://i.im5i.com/2021/02/11/hVfg3.jpg','https://i.im5i.com/2021/02/11/hVl5y.md.png','https://i.im5i.com/2021/02/11/hVr8O.jpg']

explain = on_command("我要亲亲", priority=5)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message=kiss[random.randint(0,len(kiss)-1)]
    )

explain = on_command("我要抱抱",priority=5)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message=kiss[random.randint(0,len(kiss)-1)]
    )


cfop = on_command("setu", priority=5)
@cfop.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = MessageSegment.image(setu[random.randint(0,len(setu)-1)])
    )

st = on_command("每日一图", priority=5)
@st.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = MessageSegment.image(setu[random.randint(0,len(setu)-1)])
    )

st = on_command("来一份色图", priority=5)
@st.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = MessageSegment.image(setu[random.randint(0,len(setu)-1)])
    )

ac = on_command("AC",priority=5)
@ac.handle()
async def ACAC(bot:Bot,event: Event,state: dict):
    await bot.send(
        event=event,
        message='我要AC我要AC'
    )

newyear = on_command("新年快乐kaptree",priority=5)
@newyear.handle()
async def resp(bot:Bot,event: Event,state: dict):
    await bot.send(
        event=event,
        message='新年快乐鸭，（づ￣3￣）づ╭❤～'
    )

help = on_command("查看说明",priority=5)
@help.handle()
async def resp1(bot:Bot,event: Event,state: dict):
    await bot.send(
        event=event,
        message='1.每日一句 eg:每日一句\n2.天气查询 eg:天气 成都\n3.翻译 eg:翻译 cat\n4.戳一戳 eg:手机戳我头像\n5.精彩图片 eg:每日一图/(setu)\n6.我要抱抱 eg 我要抱抱\n7.新年快乐kaptree\n8'
    )

help2 = on_command("help",priority=5)
@help2.handle()
async def resp2(bot:Bot,event: Event,state: dict):
    await bot.send(
        event=event,
        message='1.每日一句 eg:每日一句\n2.天气查询 eg:天气 成都\n3.翻译 eg:翻译 cat\n4.戳一戳 eg:手机戳我头像\n5.精彩图片 eg:每日一图/(setu)\n6.我要抱抱 eg 我要抱抱\n7.新年快乐kaptree\n8'
    )
