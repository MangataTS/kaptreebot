import json
import os
from time import sleep

import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import require

# 群发的白名单
# group_id_list=[913088980,719126877,1055277728,940568724,867600902]
group_id_list=[719126877,913088980]
scheduler = require('nonebot_plugin_apscheduler').scheduler
def get_state():
    try:
        url='https://api.iyk0.com/bilibili/user/?mid=486738984'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        val = requests.get(url, headers=headers)
        res = json.loads(val.content)
        if res['live_bf']=='直播中':
            return '直播'
        else:
            return '未直播'
    except Exception as e:
        print('get_state_error',e)

def get_message():
    try:
        driver = webdriver.Chrome(
            executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')  # 选择Chrome浏览器
        driver.get('https://live.bilibili.com/22864638')  # 打开网站  22864638
        driver.maximize_window()  # 最大化谷歌浏览器
        title = driver.find_element(By.XPATH, '//*[@id="head-info-vm"]/div/div/div[1]/div[1]/div[2]/div/div').text
        depart = driver.find_element(By.XPATH, '//*[@id="head-info-vm"]/div/div/div[1]/div[1]/div[3]/a').text
        renqi = driver.find_element(By.XPATH,'//*[@id="head-info-vm"]/div/div/div[1]/div[2]/div[3]/span').text
        sleep(1)
        try:
            driver.save_screenshot('.\\living.png')
        except BaseException as msg:
            print("%s ：截图失败！！！" % msg)
        ans="您关注的直播间开播啦！\n"+"[主题]： "+"["+title+"]\n"+"[分区]： "+"["+depart+"]\n"+"[人气]： "+"["+renqi+"]\n"+"[链接]: live.bilibili.com/22864638\n";
        driver.close()
        return ans
    except Exception as e:
        print('get_message_error', e)
        return "您关注的直播间开播啦！\n"

last_time=int(0)

@scheduler.scheduled_job('interval',seconds=10, id='bilibili_live')
async def bilibili_live():
    (bot,) = nonebot.get_bots().values()
    global last_time
    if last_time == 0:
        if get_state() == '直播':
            ans = get_message()
            path_ = os.getcwd()
            path = 'file:///' + path_ + 'living.png'
            print(path)
            for id in group_id_list:
                try:
                    await bot.send_msg(
                        message_type='group',
                        group_id=int(id),
                        message=MessageSegment.image(path) + ans
                    )
                except Exception as e:
                    last_time = 1
                    print('直播推送error：', e)
            last_time = 1
    else:
        if get_state() == '闲置':
            last_time = 0
