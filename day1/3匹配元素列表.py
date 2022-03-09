# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3匹配元素列表.py
# @ide     : PyCharm
# @time    : 2020/10/25 10:41
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day1/test1.html")

# 匹配元素列表，返回所有匹配到的元素，如果一个都匹配不到，就返回空列表
eleSli = driver.find_elements_by_tag_name("p")
print(type(eleSli))
print(eleSli[0].text)

for ele in eleSli:
    print(ele.text)
