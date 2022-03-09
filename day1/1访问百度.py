# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1访问百度.py
# @ide     : PyCharm
# @time    : 2020/10/25 9:34
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 找到搜索输入框
ele = driver.find_element_by_id("kw")
ele.send_keys("selenium")

# 点击搜索按钮
driver.find_element_by_id("su").click()

# 退出浏览器
driver.quit()
