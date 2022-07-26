from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Event, PokeNotifyEvent,LuckyKingNotifyEvent,GroupRecallNoticeEvent
import random
from nonebot.adapters.onebot.v11 import MessageSegment

a = ['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳了，戳怀孕了',
   '嘤嘤嘤，人家痛痛','我错了我错了，别戳了','桥豆麻袋,别戳老子','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？','不要啦，别戳啦','给你一拳','再摸就是狗','你这么闲吗？','代码写完了吗？','你能AK WF吗？','爬去学习']

pre = 0
poke=on_notice()
@poke.handle()
async def _(bot:Bot,event:Event):
    try:
        if isinstance(event,PokeNotifyEvent):
            if event.is_tome() and event.user_id !=event.self_id:
                l = len(a)
                k = random.randint(0,l-1)
                while pre == k:
                    k = random.randint(0,l-1)
                last = k
                await bot.send(
                    event=event,
                    message=a[k],
                    at_sender=True
                )
    except Exception as e:
        await poke.send("戳一戳插件出现故障，请联系Mangata")

chehui = on_notice()
@chehui.handle()
async def cheh(bot:Bot,event:GroupRecallNoticeEvent):
    try:
        print(event.self_id)
        if event.operator_id == event.user_id:
            await bot.send(
                    event=event,
                    message='喜欢人家就直说啊,我还没说不同意呢~',
                    at_sender=True
                  )
    except Exception as e:
        await chehui.send("撤回插件出现故障，请联系Mangata")

regbag = on_notice()
@regbag.handle()
async def redb(bot:Bot,event:LuckyKingNotifyEvent):
    try:
        atmsg = MessageSegment.at(event.target_id)
        await bot.send(
            event=event,
            message = atmsg+'恭喜你是运气王，请立即红包接力，不要不识好歹',
        )
    except Exception as e:
        await regbag.send("运气王插件出现故障，请联系Mangata")
