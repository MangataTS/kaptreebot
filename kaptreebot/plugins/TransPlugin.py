from urllib import request,parse
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event
import json
import http.client
import hashlib
import urllib
import random

from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

trans = on_command("翻译", priority=2,block=True)
@trans.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("Trans", args)  # 如果用户发送了参数则直接赋值


@trans.got("Trans", prompt="你想翻译什么呢...")
async def handle_trans(Trans: Message = Arg(), text: str = ArgPlainText("Trans")):
    try:
        text_trans =  get_baidufanyi(text)
        await trans.send(text_trans)
    except Exception as e:
        await trans.send("翻译插件出现故障，请联系Mangata")

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

def get_baidufanyi(trans: str):
    appid = '20210225000707766'  # 填写你的appid
    secretKey = 'uTcrrrrtOpHHqi4sOyc6'  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    q = trans
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        c='翻译结果: '+result['trans_result'][0]['dst']
        print (c)
        return c
    except Exception as e:
        print (e)
        return '人家还翻译不了这个呢'
    finally:
        if httpClient:
            httpClient.close()
