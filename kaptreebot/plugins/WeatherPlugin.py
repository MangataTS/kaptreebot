import urllib.request
import gzip
import json
from nonebot import on_command
from nonebot.rule import to_me

from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText


weather = on_command(cmd="天气",rule=to_me(), priority=2,block=True)


@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    try:
        city_weather = await get_weather(city_name)
        await weather.send(city_weather)
    except Exception as e:
        await weather.send("天气查询插件出现故障，请联系Mangata")




async def get_weather(city: str):
    cityname = city
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname) # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    weather_data = urllib.request.urlopen(url).read() # 发出请求并读取到weather_data
    weather_data = gzip.decompress(weather_data).decode('utf-8') # 以utf-8的编码方式解压数据
    weather_dict = json.loads(weather_data) # 将json数据转化为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        return f"这个地方人家没去过呢，要不你带我去一次叭♥~"
    elif weather_dict.get('desc') =='OK' :
        forecast = weather_dict.get('data').get('forecast')
        startoday = '城市：'+weather_dict.get('data').get('city') +'\n' \
                  +'日期：'+forecast[0].get('date') + '\n'\
                  +'温度：'+weather_dict.get('data').get('wendu') + '℃\n' \
                  +'高温：'+forecast[0].get('high') + '\n' \
                  +'低温: '+forecast[0].get('low') + '\n' \
                  +'风向：'+forecast[0].get('fengxiang') +'\n'\
                  +'风力：'+forecast[0].get('fengli') + '\n'\
                  +'天气：'+forecast[0].get('type') + '\n'\
                  +'感冒：'+weather_dict.get('data').get('ganmao') + '\n'
        return startoday
