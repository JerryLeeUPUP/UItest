# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3css高级语法.py
# @ide     : PyCharm
# @time    : 2020/10/28 20:25
"""
推荐的元素定位方式的优先级
如果能用id定位，第一顺序选择id
优先级次之，name
优先级再次，css
优先级再次，xpath


针对 css 和 xpath
相对于xpath，我们更推荐css
1、css是配合html工作，实现原理是匹配对象的原理，而xpath是配合xml工作的，xpath的原理是遍历，所以两者在设计上css性能更优秀
2、语言更加简洁明了
3、前端开发更主要是使用css，不用xpath，所以在技术方面，我们可以更容易获得帮助
"""
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day3/test.html")

ele = driver.find_element_by_css_selector("#abc")
print(ele.text)
