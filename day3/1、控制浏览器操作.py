# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1、控制浏览器操作.py
# @ide     : PyCharm
# @time    : 2020/10/28 20:01
from selenium import webdriver
import time

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")
driver.get("http://www.taobao.com")

# # 浏览器后退
# driver.back()
# time.sleep(3)
#
# # 浏览器前进
# driver.forward()
# time.sleep(3)
#
# # 刷新界面
# driver.refresh()

# 设置浏览器的高度和宽度, 数字参数的单位是像素点
driver.set_window_size(700,700)
time.sleep(3)

# 最大化，全屏展示
driver.maximize_window()
time.sleep(3)

# 最小化
driver.minimize_window()


