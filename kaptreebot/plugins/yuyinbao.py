from ctypes import Union
from requests_html import HTMLSession
import requests
from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event, Message
import random
from aiocqhttp import MessageSegment
from nonebot.permission import SUPERUSER

# 语音包指令

# 你好呀小可爱
# hello = on_command('/hello',priority=5)
# @hello.handle()
# async def hello_(bot:Bot,event:Event):
#     sst = MessageSegment.record(file='http://nightingale-audios.oss-cn-beijing.aliyuncs.com/nightingale/%E4%BD%A0%E5%A5%BD%EF%BC%8C%E5%B0%8F%E5%8F%AF%E7%88%B1.mp3?Expires=1613823346&OSSAccessKeyId=LTAI4G6EDrqvt1xhdeJAvczv&Signature=xzZGrbQUoka2XZ0nrHfCIoZKzvg%3D')
#     await bot.send(
#         event=event,
#         message=Message(sst)
#     )
# # 晚安
# wanan = on_command('/晚安',priority=5)
# @wanan.handle()
# async def wanan_(bot:Bot,event:Event):
#     sst = MessageSegment.record(file='http://nightingale-audios.oss-cn-beijing.aliyuncs.com/nightingale/%E6%99%9A%E5%AE%89%20%E5%AE%9D%E5%AE%9D%E4%B9%88%E4%B9%88%E5%93%92.mp3?Expires=1613824046&OSSAccessKeyId=LTAI4G6EDrqvt1xhdeJAvczv&Signature=7P0FwZu03EpAs42Fq6WGltIh6Fo%3D')
#     await bot.send(
#         event=event,
#         message=Message(sst)
#     )
#
# # 小哥哥别生气了
# shenqi = on_keyword(['生气','气死'],priority=5)
# @shenqi.handle()
# async def shenqi_(bot:Bot,event:Event):
#     sst = MessageSegment.record(file='http://nightingale-audios.oss-cn-beijing.aliyuncs.com/nightingale/%E3%80%82%E5%93%8E%E5%91%80%E5%A5%BD%E7%9A%84%E5%95%A6%20%E5%B0%8F%E5%93%A5%E5%93%A5%E4%B8%8D%E8%A6%81%E7%94%9F%E6%B0%94%E4%BA%86%E5%98%9B.mp3?Expires=1613824347&OSSAccessKeyId=LTAI4G6EDrqvt1xhdeJAvczv&Signature=j%2FJn%2FPG4oh3HxDYR60%2F0hDCOafw%3D')
#     await bot.send(
#         event=event,
#         message=Message(sst)
#     )
#
# # 我已经躺在床上了
# zhijie = on_command('今晚到我房间来',priority=5,permission=SUPERUSER)
# @zhijie.handle()
# async def zhijie_(bot:Bot,event:Event):
#     sst = MessageSegment.record(file='http://nightingale-audios.oss-cn-beijing.aliyuncs.com/nightingale/%E3%80%82%E7%8E%B0%E5%9C%A8%E5%B7%B2%E7%BB%8F%E8%BA%BA%E5%9C%A8%E4%BA%86%E5%BA%8A%E4%B8%8A.mp3?Expires=1613824906&OSSAccessKeyId=LTAI4G6EDrqvt1xhdeJAvczv&Signature=QyzbgnIEQ82PGA13fJiutDr2e6A%3D')
#     await bot.send(
#         event=event,
#         message=Message(sst)
#     )
