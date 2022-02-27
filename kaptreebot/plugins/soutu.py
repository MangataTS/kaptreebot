import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, Event

from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

ND = on_command("网图",aliases={"搜图"}, priority=2,block=True)
@ND.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("Name", args)  # 如果用户发送了参数则直接赋值


@ND.got("Name", prompt="你想找哪个人物呀？小可爱~")
async def handle_city(Name: Message = Arg(), sname: str = ArgPlainText("Name")):
    try:
        print("-----网图测试")
        print(sname)
        print("-----网图测试")
        url = f'https://api.iyk0.com/swt/?msg={sname}'
        url = str(requests.get(url).text)
        await ND.send(MessageSegment.image(url))
    except Exception as e:
        await ND.send("搜图插件出现故障，请联系Mangata")
