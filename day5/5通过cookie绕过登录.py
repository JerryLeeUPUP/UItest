# -*- coding: utf-8  -*-
# @File     : 5通过cookie绕过登录.py
# @author   : Jerry
# @datetime : 2022/3/15 9:33
# @software : PyCharm
from selenium import webdriver

#屏蔽 windows.navigator.webdriver
options = webdriver.ChromeOptions()
# 设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)
driver.get("https://qa2-www.yunquna.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_css_selector("div.common-top-bar-info-operate-area").click()
# 这是之前获取到的 cookies, 记得把每一个字典的 expiry 注释，防过期
# Cookies = [{'domain': '.yunquna.com',
#             #'expiry': 1647399160,
#             'httpOnly': False,
#             'name': 'ac',
#             'path': '/',
#             'secure': False,
#             'value': '%E4%B8%AD%E5%9B%BD|%E6%B9%96%E5%8C%97|%E6%AD%A6%E6%B1%89'},
#             {'domain': '.yunquna.com',
#             #'expiry': 1678416758,
#             'httpOnly': False,
#             'name': 'fg',
#             'path': '/',
#             'secure': False,
#             'value': '1f8453116198017e0fd3e0f64a3d8b9f'},
#             {'domain': '.yunquna.com',
#             #'expiry': 1678416757,
#             'httpOnly': True,
#             'name': 'qa2_track_id',
#             'path': '/',
#             'secure': False,
#             'value': '16db0d7a21b671d19b91453f3430575e'},
#             {'domain': '.yunquna.com',
#             #'expiry': 1678416757,
#             'httpOnly': False,
#             'name': 'lk',
#             'path': '/',
#             'secure': False,
#             'value': '7259188e-55fb-44bf-9f0a-d21f8ed8b0f2'},
#             {'domain': '.yunquna.com',
#             #'expiry': 7954512760,
#             'httpOnly': False,
#             'name': 'sensorsdata2015jssdkcross',
#             'path': '/',
#             'secure': False,
#             'value': '%7B%22distinct_id%22%3A%2217f8b7de0847c9-071ad43ea5e40c-594f2612-2073600-17f8b7de085b59%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTdmOGI3ZGUwODQ3YzktMDcxYWQ0M2VhNWU0MGMtNTk0ZjI2MTItMjA3MzYwMC0xN2Y4YjdkZTA4NWI1OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217f8b7de0847c9-071ad43ea5e40c-594f2612-2073600-17f8b7de085b59%22%7D'},
#             {'domain': '.yunquna.com',
#             #'expiry': 1647359999,
#             'httpOnly': False,
#             'name': 'sajssdk_2015_cross_new_user',
#             'path': '/',
#             'secure': False,
#             'value': '1'}]    # 是个列表,列表里是一个个的字典



#清除所有cookie
driver.delete_all_cookies()
#for cookie in Cookies:
    #添加cookie
#    driver.add_cookie(cookie)
#driver.refresh()