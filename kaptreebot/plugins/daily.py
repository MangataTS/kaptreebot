import requests
import datetime
import re
import random
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event

dic_m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
dic_d = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
          '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']


def get_news():
    i = dic_m[datetime.datetime.now().month-1]
    j = dic_d[datetime.datetime.now().day-1]

    m = dic_m[random.randint(0,11)]
    d = dic_d[random.randint(0,28)]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }

    url = 'http://sentence.iciba.com/index.php?callback=jQuery19007923698552257794_1589363317323&c=dailysentence&m=getdetail&title=2020-' + \
          m + '-' + d + '&_=1589363317329'
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    a = res.text
    print(a)
    b = re.findall('"note":"(.*?)",', a, re.S)
    c = b[0].encode('ascii').decode('unicode_escape')
    c = i + '月' + j + '日：' + c
    print('每日一句输出: ',c)
    return c

explain = on_command("每日一句", priority=2)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message=get_news()
    )
