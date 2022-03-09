# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 4键盘事件.py
# @ide     : PyCharm
# @time    : 2020/10/30 20:44
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
driver.get("http://www.baidu.com")

ele = driver.find_element_by_id("kw")
# 对文本框输入内容
ele.send_keys("selenium")
# 退格键
ele.send_keys(Keys.BACK_SPACE)

# 输入空格键+教程
ele.send_keys(Keys.SPACE)
ele.send_keys("教程")
# 制表符
ele.send_keys(Keys.TAB)
# 回退键
ele.send_keys(Keys.ESCAPE)
# 回车键
ele.send_keys(Keys.ENTER)
ele.send_keys(Keys.COMMAND)
