# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 5分步骤元素定位.py
# @ide     : PyCharm
# @time    : 2020/10/25 10:48
from selenium.webdriver.common.by import By
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day1/test1.html")

# 元素层级很深，或一次定位太过复杂，可以分步骤定位
# 先定位到元素的父元素
ele = driver.find_element_by_tag_name("div")
# 再根据父元素，去定位子元素
ele1 = ele.find_element_by_tag_name("li")
print(ele1.text)
