# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 上次作业.py
# @ide     : PyCharm
# @time    : 2020/10/28 21:57
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
driver.implicitly_wait(5)
# 访问网址
driver.get("https://www.vmall.com")

# 获取所有的一级菜单
liSli = driver.find_elements_by_css_selector("#category-block ol > li")
for li in liSli:
    # 打印一级菜单名称
    print("一级菜单:", li.find_element_by_css_selector("div:nth-child(3) span").text)
    # 鼠标悬停到一级菜单
    ActionChains(driver).move_to_element(li).perform()
    # 匹配每一个二级菜单

    liSli2 = li.find_elements_by_css_selector("div:nth-child(4) span")
    for li2 in liSli2:
        print("\t", li2.text)

# print("="*20)
# # 向下滚动
# driver.execute_script("window.scrollBy(0, 900)")
# # 找到每一个
# liSli = driver.find_elements_by_xpath("//div[@class=\"span-968 fl\"]/ul[@class=\"grid-list clearfix\"]/li")
# for li in liSli:
#     if not li.find_elements_by_xpath(".//em/span"):
#         continue
#
#     # 获取商品名称
#     goodName = li.find_element_by_xpath(".//div[@class=\"grid-title\"]").text
#     # 获取商品价格
#     goodPrice = li.find_element_by_xpath(".//p[@class=\"grid-price\"]").text
#     print("{}， 价格{}".format(goodName, goodPrice))

