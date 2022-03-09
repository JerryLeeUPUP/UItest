# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1窗口截图.py
# @ide     : PyCharm
# @time    : 2020/10/30 20:01
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 截屏，截取整个页面
driver.get_screenshot_as_file("./all.png")
# 截屏，截取单个元素
ele = driver.find_element_by_id("kw")
ele.screenshot("./ele.png")

driver.quit()
