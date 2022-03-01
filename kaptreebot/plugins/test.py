# #
# import json
# import random
# import re
# import urllib
# from asyncio import Event
# from urllib.request import urlopen
# from time import sleep
#
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# # import time
# #
#
# driver = webdriver.Chrome()  # 选择Chrome浏览器
# driver.get('https://live.bilibili.com/631')  # 打开网站
# driver.maximize_window()  # 最大化谷歌浏览器
# html = driver.page_source
# tt = driver.find_element(By.XPATH, '//*[@id="head-info-vm"]/div/div/div[1]/div[1]/div[1]').text
# print(tt)
# sleep(1)
# try:
#     picture_url=driver.save_screenshot('.\\living.png')
#     print("%s ：截图成功！！！" % picture_url)
# except BaseException as msg:
#     print("%s ：截图失败！！！" % msg)
# driver.close()
#
import json
import requests


def get_state():
    try:
        url='http://api.iyk0.com/bilibili/user/?mid=486738984'
        val = requests.get(url)
        res = json.loads(val.content)
        if res['live_bf']=='直播中':
            return ('直播')
        else:
            return ('未直播')
    except Exception as e:
        print('get_state_error',e)
        return ('未直播')

print(get_state())