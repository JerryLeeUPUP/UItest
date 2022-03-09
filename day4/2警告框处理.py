# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2警告框处理.py
# @ide     : PyCharm
# @time    : 2020/10/30 20:08
from selenium import webdriver
import time

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/test/script/study/seleniumStu/day4/test1.html")

# # 触发对话框
# driver.find_element_by_id("bu1").click()
# time.sleep(3)
# # 获取对话框对象
# al = driver.switch_to.alert
# al.accept()  # 确认对话框

# # 触发确认框
# driver.find_element_by_id("bu2").click()
# time.sleep(3)
# # 获取确认框对象
# al = driver.switch_to.alert
# al.dismiss()  # 取消确认框


# 触发提示框
driver.find_element_by_id("bu3").click()
# 获取提示框对象
al = driver.switch_to.alert
al.send_keys("你看不到我")  # 发送文本至提示框
time.sleep(5)
print(al.text)  # 返回警告框中的文本信息
al.accept()
