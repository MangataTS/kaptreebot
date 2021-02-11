from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, PokeNotifyEvent
from nonebot.adapters.cqhttp.message import Message
import random
poke=on_notice()
a=['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳了，戳怀孕了',
   '戳🔨戳','我错了我错了，别戳了','桥豆麻袋,别戳老子','再戳砍手','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？']
@poke.handle()
async def _(bot:Bot,event:Event):
    if isinstance(event,PokeNotifyEvent):
        if event.is_tome() and event.user_id!=event.self_id:
            await bot.send(
        event=event,
        message=a[random.randint(0,len(a)-1)]
        )
    else:
        await poke.finish()
