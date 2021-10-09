import requests
import random
from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event
from requests_html import HTMLSession

def get_qinhua():
    url='https://api.lovelive.tools/api/SweetNothings/1/Serialization/Text?genderType=M'
    res = requests.get(url)
    print('情话:',res.text)
    return str(res.text)

def get_lvcha():
    url='https://api.lovelive.tools/api/SweetNothings/1/Serialization/Text?genderType=F'
    res = requests.get(url)
    print('绿茶:',res.text)
    return str(res.text)

def get_news():
    url='https://api.ixiaowai.cn/tgrj/index.php'
    res = requests.get(url)
    b = res.text
    c = b.replace('*','')
    print('情感语录1:',c)
    return c

def get_new2():
    url='https://du.liuzhijin.cn/dog.php'
    session = HTMLSession()
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    r = session.get(url,headers=headers)
    sel ='#text'
    s = r.html.find(sel)
    str1 = s[0].text
    print('情感语录2:',str1)
    return str1

exlpain = on_command("情感语录",aliases={'舔狗日记'} ,priority=2)
@exlpain.handle()
async def slove(bot: Bot, event: Event, state: dict):
    if int(event.get_user_id())!= event.self_id:
        str1=''
        if(random.randint(0,1)):
            str1=get_new2()
        else:
            str1=get_news()
        await bot.send(
            event=event,
            message=str1,
            at_sender=True
        )

qinghua = on_keyword("情话",priority=2)
@qinghua.handle()
async def qinghua_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_qinhua()
        )

lvcha= on_keyword("绿茶",priority=2)
@lvcha.handle()
async def lvcha_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_lvcha()
        )
