# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3隐式等待.py
# @ide     : PyCharm
# @time    : 2020/10/26 20:45
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")
# 隐式等待
# 当代码执行到某个元素定位的时候，如果能找到，则继续执行
# 如果找不到则以轮询的方式不断判断元素是否存在
# 若中间找到了，则不再等，继续往下执行
# 若达到最大时间还找不到，就抛出超时异常
# 隐式等待只需要申明一次，申明之后的所有元素定位都生效
# 而显示等待只对主动声明的元素定位有效
driver.implicitly_wait(5)

# 之后的每一次元素等待都是有效的
driver.find_element_by_css_selector("fffff")
driver.find_element_by_css_selector("xxxx")

