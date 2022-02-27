# import base64
# import json
#
# from bs4 import BeautifulSoup
#
# import time
# import os
# from selenium import webdriver
#
#
# # encoding:utf-8
# import requests
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
# def download_img(img_url,cookiestr):
#     print (img_url)
#     headers_cookie = {
#         "Cookie": str(cookiestr)  # 通过接口请求时需要cookies等信息
#     }
#     r = requests.get(img_url,headers=headers_cookie)
#     print(r.status_code) # 返回状态码
#     if r.status_code == 200:
#         open('G:\\img.png', 'wb').write(r.content) # 将内容写入图片
#         print("--------done----------")
#     del r
# def ocr():
#     request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
#     f = open(r'G:\img.png', 'rb')
#     img = base64.b64encode(f.read())
#     params = {"image": img}
#     access_token = '[24.4bb361db1fa36f72b47627f5dc4b5706.2592000.1640622341.282335-25244542]'
#     request_url += "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     if response:
#         c = response.json()
#         k = c['words_result'][0]['words'].strip(' ')
#         print('验证结果是： ', k)
#         return k
#     else:
#         return "OCR_error"
#
#
#
# # 环境配置
# chromedriver = "C:\Program Files\Google\Chrome\Application"
# os.environ["webdriver.ie.driver"] = chromedriver
#
# driver = webdriver.Chrome()  # 选择Chrome浏览器
# driver.get('http://acm.mangata.ltd/login')  # 打开网站
# driver.maximize_window()  # 最大化谷歌浏览器
# cookies = driver.get_cookies()
#
#
# html = driver.page_source
# soup = BeautifulSoup(html,'lxml')
# link = 'http://acm.mangata.ltd/login'
#
#
# uname = "1196991321@qq.com"  # 请替换成你的用户名
# password = ""  # 请替换成你的密码
# #print(driver.page_source)
# driver.find_element(By.PARTIAL_LINK_TEXT,'uname').click()  # 点击用户名输入框
# driver.find_element(By.NAME,'uname').clear()  # 清空输入框
# driver.find_element(By.NAME,'uname').send_keys(uname)  # 自动敲入用户名
#
# driver.find_element(By.NAME,'password').click()  # 点击密码输入框
# driver.find_element(By.NAME,'password').clear()  # 清空输入框
# driver.find_element(By.NAME,'password').send_keys(password)  # 自动敲入密码
#
#
#
#
# # time.sleep(1)
#
# driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div/div/form/div[5]/div/div/input[2]').click()# 点击“登录”按钮
# for i in range(1016,1275):#1233
#     ipp='http://acm.mangata.ltd/p/old'
#     ipp+=str(i)
#     ipp+='/edit'
#     #print("ipp=",ipp)
#     driver.get(ipp)
#     try:
#         tt = driver.find_element(By.XPATH, '//*[@id="panel"]/div[3]/div/div[1]/div/div/form/div[2]/div[1]/label/div/input').get_attribute('value')
#         tt=tt.replace(" ",",")
#         tt=tt.replace("-",",")
#         # print(tt)
#         driver.find_element(By.NAME,'tag').click()  # 点击标签框
#         #
#         driver.find_element(By.NAME,'tag').clear()  # 清空框
#         driver.find_element(By.NAME,'tag').send_keys(tt)  # 自动敲入用户名
#         #
#         driver.find_element(By.XPATH,'//*[@id="panel"]/div[3]/div/div[1]/div/div/form/div[5]/div/button[1]').click()# 点击“保存”按钮
#     except NoSuchElementException:
#         print("no page ",ipp)
# # win32api.keybd_event(122, 0, 0, 0)  # F11的键位码是122，按F11浏览器全屏
# # win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#
# # driver.close()
#
#
#
#
#
#
#
#
# # 0.9415354059892882
# # 0.9415354059892882