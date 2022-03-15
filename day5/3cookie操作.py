# -*- coding: utf-8  -*-
# @File     : 3cookie操作.py
# @author   : Jerry
# @datetime : 2022/3/14 16:15
# @software : PyCharm

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

cookieSli = driver.get_cookies()


print(cookieSli)