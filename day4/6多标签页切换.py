# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 5多标签页切换.py
# @ide     : PyCharm
# @time    : 2020/10/30 21:23
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#hotsearch-content-wrapper > li:nth-child(1)").click()

# 获取当前所有打开窗口的句柄
all_handles = driver.window_handles

for handle in all_handles:
    driver.switch_to.window(handle)
    if driver.title == "五中全会公报中这些提法令人关注_百度搜索":
        print("匹配成功")
        break

print(driver.title)
driver.find_element_by_css_selector("a.s-tab-item.s-tab-video").click()
