import os
from time import sleep

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
        driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')  # 选择Chrome浏览器
        driver.get('https://live.bilibili.com/22864638')  # 打开网站
        driver.maximize_window()  # 最大化谷歌浏览器
        html = driver.page_source
        tt = driver.find_element(By.XPATH, '//*[@id="head-info-vm"]/div/div/div[1]/div[1]/div[1]').text
        driver.close()
        return str(tt)
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
            path = 'file:///' + path_ + '\kaptreebot\plugins\living.png'
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
