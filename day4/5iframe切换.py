# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 5iframe切换.py
# @ide     : PyCharm
# @time    : 2020/10/30 21:06
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("file:///D:/test/script/study/seleniumStu/day4/test3.html")

# 先找到内嵌网页
ifa = driver.find_element_by_css_selector("iframe:nth-child(3)")
# 切入内嵌网页
driver.switch_to.frame(ifa)
driver.find_element_by_css_selector("input[id=\"kw\"]").send_keys("今年双十一，一号就开始啦")

# 切回主页面
driver.switch_to.default_content()
