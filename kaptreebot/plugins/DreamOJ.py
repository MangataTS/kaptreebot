import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message
import random
from nonebot.adapters.onebot.v11 import MessageSegment
import json
import re
from lxml import etree
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

def recent_contest():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    url="http://algcontest.rainng.com"
    val=requests.get(url,headers=headers)
    res=json.loads(val.content)
    sum=""
    i = 0
    for it in res:
        i=i+1
        sum = sum  + '[比赛名称]： '
        sum = sum + it['name']
        sum = sum + '\n[比赛时间]： '
        sum = sum + it['startTime']
        sum = sum + '\n[比赛链接]： '
        sum = sum + it['link']
        sum = sum + '\n'
        if i == 3:
            break
    return sum

Rcontest = on_command("最近比赛", priority=2,block=True)
@Rcontest.handle()
async def Rcontest_(bot: Bot, event: Event):
    try:
        if int(event.get_user_id()) != event.self_id:
            await bot.send(
                event=event,
                message=str(recent_contest())
            )
    except Exception as e:
        await Rcontest.send("最近比赛插件出现故障，请联系Mangata")



def get_least_cf():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    url = "http://algcontest.rainng.com"
    val = requests.get(url, headers=headers)
    res = json.loads(val.content)
    sum = ""
    i = 0
    for it in res:
        if it['oj'] == 'CodeForces':
            sum = '找到最近一场CodeForces比赛：\n'
            sum = sum + '[比赛名称]： '
            sum = sum + it['name']
            sum = sum + '\n[比赛时间]： '
            sum = sum + it['startTime']
            sum = sum + '\n[比赛链接]： '
            sum = sum + it['link']
            sum = sum + '\n'
            break
    if sum == "":
        sum = "最近没有Codeforces比赛噢，开始摆烂吧！"
    return sum

codeforces=on_command(cmd="cf",priority=2,block=True)
@codeforces.handle()
async def codeforces_():
    try:
        await codeforces.send(get_least_cf())
    except Exception as e:
        await codeforces.send("最近CF插件出现故障，请联系Mangata")


def honor(num:int):
    if num <= 50:
        return "坚韧黑铁"
    elif num <= 150:
        return "英勇黄铜"
    elif num <= 300:
        return "不屈白银"
    elif num <= 500:
        return "荣耀黄金"
    elif num <= 650:
        return "华贵铂金"
    elif num <= 800:
        return "璀璨钻石"
    elif num <= 1000:
        return "超凡大师"
    elif num <= 1500:
        return "傲世宗师"
    else:
        return "最强王者"


def get_usr(id:int):
    url="http://acm.mangata.ltd/user/"+str(id)
    ua_headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    # 网页代码
    response = requests.get(url=url, headers=ua_headers).text
    # 转换为etree对象
    tree = etree.HTML(response)
    img_lst = tree.xpath('//*[@id="panel"]/div[3]/div/div[1]/div[1]/div[1]/div/div/div[2]/p[2]/text()')
    message = img_lst[0].split(',')
    slove_problem=int(re.findall("\d+", message[0])[0])
    return "\n[当前段位]： [" + honor(slove_problem)+"]"


# Dream OJ 查询用户
DOJ_USER = on_command("DOJ",aliases={'find','查找','查找用户'}, priority=2,block=True)
@DOJ_USER.handle()
async def DOJ_USER_(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("name", args)  # 如果用户发送了参数则直接赋值


@DOJ_USER.got("name", prompt="请输入你想查询的用户名...")
async def handle_DOJ_USER(name: Message = Arg(), sname: str = ArgPlainText("name")):
    try:
        url="http://acm.mangata.ltd/api/?"
        headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
            }
        query="query {user(uname: \"" + sname + "\") {uname,mail,loginat,regat,role,avatarUrl,_id}}"
        url = url + query
        val=requests.get(url,headers=headers)
        res=json.loads(val.content)
        it=res['data']['user']
        ans=""
        if res['data']['user'] == None:
            ans = ans + "查无此人"
            await DOJ_USER.send(ans)
        else:
            id=it['_id']
            ans ="\n[用户昵称]： [" + it['uname'] + "]"
            ans = ans + str(get_usr(id))
            ans = ans + "\n[上次登陆]： [" + it['loginat'] + "]"
            ans = ans + "\n[注册时间]： [" + it['regat'] + "]"
            ans = ans + "\n[用户身份]： [" + it['role'] + "]"
            qq=str(it['mail'])
            ava = "https://q1.qlogo.cn/g?b=qq&nk="
            if qq.find("@qq.com") == -1:
                ava="http://acm.mangata.ltd/file/2/12.jpg"
            else:
                qq=qq.strip('@qq.com')
                ava=ava+qq+"&s=160"
            await DOJ_USER.send(MessageSegment.image(ava) + ans)
    except Exception as e:
        await DOJ_USER.send("DOJ用户插件出现故障，请联系Mangata")

#获取随机题目
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
        return str("题目已被隐藏请再次输入！")
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
        ans = "[题目名称]： " + it['title']
        ans = ans + "\n[题目连接]： " + link
        ans = ans + "\n[算法标签]： " + tag
        ans = ans + "\n[总提交数]： " + str(it['nSubmit'])
        ans = ans + "\n[总通过数]： " + str(it['nAccept'])
        ans = ans + "\n[预估难度]： " + str(it['difficulty'])
        ans = ans + "\n骚年快来挑战吧！别忘了写题解噢！"
        return ans



# 每日一题
DOJ_PROBLEM = on_command("随机题目",aliases={'每日一题'}, priority=2,block=True)
@DOJ_PROBLEM.handle()
async def DOJ_PROBLEM_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        ans = get_problem()
        await bot.send(
            event = event,
            message=ans
        )