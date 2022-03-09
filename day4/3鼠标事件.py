# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3鼠标事件.py
# @ide     : PyCharm
# @time    : 2020/10/30 20:27
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 定位到需要悬停的元素
above = driver.find_element_by_link_text("更多")
# 对定位到的元素进行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
# 右击
ActionChains(driver).context_click(above).perform()
# 双击
ActionChains(driver).double_click(above).perform()

# 拖动, 第一个参数是起始元素，也就是被拖动的元素，第二个参数是目标元素，也就是拖动到的位置
ActionChains(driver).drag_and_drop(startEle, targetEle).perform()
