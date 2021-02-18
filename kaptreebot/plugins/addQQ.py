from nonebot import on_request
from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import FriendRequestEvent,FriendAddNoticeEvent

add = on_request()
@add.handle()
async def add_(bot:Bot,event:FriendRequestEvent):
    await event.approve(bot)


msgadd = on_notice()
@msgadd.handle()
async def sendmsg_(bot:Bot,event:FriendAddNoticeEvent):
    await bot.send(
        event=event,
        message='请输入help，然后和我一起玩叭',
    )
