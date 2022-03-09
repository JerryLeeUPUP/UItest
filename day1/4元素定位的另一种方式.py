# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 4元素定位的另一种方式.py
# @ide     : PyCharm
# @time    : 2020/10/25 10:45
from selenium.webdriver.common.by import By
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day1/test1.html")

# 根据id属性定位，第一个参数填定位方法，第二个参数填表达式
ele = driver.find_element(By.ID, "abc")
# 用这种方式匹配元素列表
ele = driver.find_elements(By.TAG_NAME, "p")
