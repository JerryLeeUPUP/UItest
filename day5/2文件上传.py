# -*- coding: utf-8  -*-
# @File     : 2文件上传.py
# @author   : Jerry
# @datetime : 2022/3/14 15:31
# @software : PyCharm
from selenium import webdriver
import win32com.client
import time
#创建浏览器驱动对象
driver = webdriver.Chrome()
#访问网址
driver.get("https://tinypng.com/")

#对于input 标签实现的文件上传功能，我们可以直接将其看作是一个输入框
#即可以用send_keys 指定本地文件路径的方式来实现文件上传
#driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("E:\python\\UI_study\day5\\test.html")

#对于非input标签实现的上传功能，我们可以通过模拟键盘敲击的方式实现
#注意：1、输入法必须为英文状态 2、操作期间，不要操作键盘鼠标
#触发文件上传的操作，如下
driver.find_element_by_css_selector("figure.icon").click()
sh = win32com.client.Dispatch("WScript.shell")
time.sleep(3)
sh.Sendkeys("E:\python\\UI_study\day5\\test.html\r\n") #\r\n 在选择文件弹框中输入的文件地址后，模拟回车的动作确定，\r\n即回车+换行