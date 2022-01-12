from typing import Dict, List
import psutil
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment
from nonebot.adapters.cqhttp import GROUP_ADMIN, GROUP_OWNER
from nonebot.adapters.cqhttp import GroupMessageEvent


def cpu_status() -> float:
    return psutil.cpu_percent(interval=1)  # type: ignore


def per_cpu_status() -> List[float]:
    return psutil.cpu_percent(interval=1, percpu=True)  # type: ignore


def memory_status() -> float:
    return psutil.virtual_memory().percent


status = on_command("系统状态",aliases={'status'},priority=2)
@status.handle()
async def status_(bot:Bot,event: Event,state: dict):
    if event.get_user_id != str(event.self_id):
        mess = 'CPU占用率： '+str(cpu_status())+'%\n'+'内存占用率： '+str(memory_status())
        if await GROUP_ADMIN(bot, event):
            await bot.send(
                event=event,
                message='尊贵的管理员：\n'+mess
            )
        elif await GROUP_OWNER(bot, event):
            await bot.send(
                event=event,
                message='尊贵的群主：\n' + mess
            )
        else:
            await bot.send(
                event=event,
                message='底层群员没有查看权限！一边凉快呆着吧\n'
            )


