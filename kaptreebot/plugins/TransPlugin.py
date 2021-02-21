from urllib import request,parse
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json


trans = on_command("翻译", priority=2)
@trans.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数
    if args:
        state["trans"] = args  # 如果用户发送了参数则直接赋值


@trans.got("trans", prompt="你想翻译什么呢...")
async def handle_trans(bot: Bot, event: Event, state: dict):
    text = state["trans"]
    text_trans = await get_trans(text)
    await trans.finish(text_trans)


async def get_trans(trans: str):
    base_url = 'https://fanyi.baidu.com/sug'
    # 构建请求对象
    data = {
        'kw': trans
    }
    data = parse.urlencode(data)
    # 模拟浏览器
    header = {"User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=header)
    res = request.urlopen(req)
    # 获取响应的json字符串
    str_json = res.read().decode('utf-8')
    # 把json转换成字典
    myjson = json.loads(str_json)
    try:
        transinfo = myjson['data'][0]['v']
    except Exception as e:
        return f"翻译错误：{e}"
    else:
        return f"{trans}的翻译内容：{transinfo}"
