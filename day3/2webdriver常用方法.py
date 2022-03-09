# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2webdriver常用方法.py
# @ide     : PyCharm
# @time    : 2020/10/28 20:13
from selenium import webdriver
import time

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# # send_keys 向文本框元素输入内容
# driver.find_element_by_id("kw").send_keys("这是文本内容")
# time.sleep(3)
# # clear 清除文本框元素的内容
# driver.find_element_by_id("kw").clear()
#
# # send_keys 向文本框元素输入内容
# driver.find_element_by_id("kw").send_keys("python")
# # click 点击元素
# driver.find_element_by_id("su").click()

# 获取元素的属性值
ele = driver.find_element_by_id("su")
print(ele.get_attribute("value"))
# 检测元素是否可见
print(ele.is_displayed())
# 获取元素的文本值
print(ele.text)
# 返回元素的尺寸
print(ele.size)
