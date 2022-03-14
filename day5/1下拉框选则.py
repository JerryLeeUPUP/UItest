# -*- coding: utf-8  -*-
# @File     : 1下拉框选则.py
# @author   : Jerry
# @datetime : 2022/3/14 14:03
# @software : PyCharm
from selenium.webdriver.support.select import Select
from selenium import webdriver

#创建浏览器驱动对象
driver = webdriver.Chrome()
#访问网址
driver.get("E:\python\\UI_study\day5\\test.html")

#定位到下拉框元素
ele = driver.find_element_by_id("abc")
#根据元素的value属性选则
#Select(ele).select_by_value("p2")
#根据下标选择
#Select(ele).select_by_index(2)
#根据下拉框的文本选择
Select(ele).select_by_visible_text("月薪三万")