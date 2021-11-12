import requests
import json
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event


def get_news():
    url ='https://v1.hitokoto.cn/'
    res = requests.get(url)
    c = json.loads(res.text)
    ans = c['hitokoto']+'---->'+c['from']
    print(ans)
    return ans

explain = on_command("每日一句", priority=2)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=get_news()
        )

