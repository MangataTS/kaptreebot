import json
import nonebot
import requests
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import require
import random


# 群发的白名单
group_id_list=[913088980,719126877,1055277728,940568724,867600902]

scheduler = require('nonebot_plugin_apscheduler').scheduler
# 获取随机题目
def get_problem():
    url="http://acm.mangata.ltd/api/?"
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    id=str(random.randint(1,1786))
    query="query{problem(id:" + id + "){pid,title,nSubmit,nAccept,difficulty,tag}}"
    url = url + query
    print(url)
    val=requests.get(url,headers=headers)

    res=json.loads(val.content)
    print(res)
    it=res["data"]["problem"]
    if it == None:
        return str("题目出错请联系Mangata！")
    else:
        link="http://acm.mangata.ltd/p/" + it['pid']
        tag = ""
        l = len(it['tag'])
        j = 1
        for i in it['tag']:
            if j < l:
                tag = tag + i + "、"
            else:
                tag = tag + i
            j=j+1
        ans = "题目名称： " + it['title']
        ans = ans + "\n题目连接： " + link
        ans = ans + "\n算法标签： " + tag
        ans = ans + "\n总提交数： " + str(it['nSubmit'])
        ans = ans + "\n总通过数： " + str(it['nAccept'])
        ans = ans + "\n预估难度： " + str(it['difficulty'])
        ans = ans + "\n骚年快来挑战吧！别忘了写题解噢！"
        return ans

@scheduler.scheduled_job('cron', hour='15',minute='41', id='problem')
async def problem():
    (bot,) = nonebot.get_bots().values()
    text = "\n快冲！今天的每日一题：\n"
    text = text + get_problem()
    url = 'http://acm.mangata.ltd/file/2/learn.jpg'

    for id in group_id_list:
        try:
            await bot.send_msg(
                message_type="group",
                group_id=int(id),
                message=MessageSegment.image(url) + text
            )
        except Exception as e:
            print(e)
