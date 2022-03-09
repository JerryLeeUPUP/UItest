# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2元素定位方法.py
# @ide     : PyCharm
# @time    : 2020/10/25 10:07
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day1/test1.html")

"""
# 通过 id 属性进行定位，只返回匹配到的第一个元素，如果找不到就报错
ele = driver.find_element_by_id("abc")
print(ele.text)

# 通过name属性定位，只返回匹配到的第一个元素，如果找不到就报错
ele = driver.find_element_by_name("abc")
print(ele.text)

# 根据 xpath 定位，
ele = driver.find_element_by_xpath("/html/body/div/ul/li")
print(ele.text)

# 根据 css 表达式定位
ele = driver.find_element_by_css_selector("body > div > ul > li")
print(ele.text)

# 根据链接文本定位
ele = driver.find_element_by_link_text("这里是百度")
ele.click()

# 根据链接文本定位，模糊匹配
ele = driver.find_element_by_partial_link_text("已停运")
ele.click()

# 根据 tag name 定位
ele = driver.find_element_by_tag_name("p")
print(ele.text)
"""

# 根据 class 属性定位
ele = driver.find_element_by_class_name("abc")
print(ele.text)
