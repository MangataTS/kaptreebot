import requests
from nonebot import on_command
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.typing import T_State

ND = on_command("网图", priority=5)


@ND.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.message).strip()
    if args:
        state["Name"] = args
        print(state["Name"], args)


@ND.got("Name", prompt="你想找哪个人物呀？小可爱~")
async def handle_city(bot: Bot, event: Event, state: T_State):
    n = state["Name"]
    print("-----网图测试")
    print(n)
    print("-----网图测试")
    url = f'https://api.iyk0.com/swt/?msg={n}'
    da = requests.get(url).text
    tu = [{
        "type": "image",
        "data": {
            "file": da
        }
    }]
    await ND.send(Message(tu))
