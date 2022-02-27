from nonebot import on_request
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import FriendRequestEvent,FriendAddNoticeEvent,GroupRequestEvent

add_friend = on_request()
@add_friend.handle()
async def add_friend_(bot:Bot,event:FriendRequestEvent):
    await event.approve(bot)

add_group = on_request()
@add_group.handle()
async def add_group(bot:Bot,event:GroupRequestEvent):
    await event.approve(bot)

friend_add = on_notice()
@friend_add.handle()
async def friend_add_(bot:Bot,event:FriendAddNoticeEvent):
    await bot.send(
        event=event,
        message='请输入help，然后和我一起玩叭',
    )

group_add = on_notice()
@group_add.handle()
async def group_add_(bot:Bot,event:GroupRequestEvent):
    await bot.send(
        event=event,
        message='请输入help，然后和我一起玩叭',
    )