# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1、获取断言信息.py
# @ide     : PyCharm
# @time    : 2020/10/26 20:08
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 获取当前页面的标题
print(driver.title)

# 获取当前页面的url
print(driver.current_url)

# 获取 标签对之间的文本信息
#   标签元素如果不展示在界面上，获取结果为空
#   如果标签对中间没有值，获取结果为空
#   如input之类的标签，获取结果也是空
ele = driver.find_element_by_css_selector("#s-hotsearch-wrapper > div > a.hot-title > div")
print(ele.text)

# 获取元素某个属性的值
print(ele.get_attribute("class"))
