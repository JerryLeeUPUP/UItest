# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2显示等待.py
# @ide     : PyCharm
# @time    : 2020/10/26 20:23
"""
显示等待
显示等待使webdriver等待某个条件成立，当条件成立的时候，继续执行
当条件不成立的时候，进入等待状态，直到最大时间，抛出超时异常
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 当代码执行到显示等待，会去检查元素是否存在
# 如果存在则继续执行，如果不存在，则每隔0.5秒执行一次
# 若 5 秒内的某一次检查到了元素，则不再等待，继续往下执行
# 若直到最大时长 5 秒钟，还等不到元素，就抛出超时异常
ele = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#s-hotsearch-wrapper > div > a.hot-title > div")
    )
)
print(ele.text)

# 显示等待只对声明了的生效，这一行代码没有声明显示等待，就不会进入显示等待的逻辑
ele = driver.find_element_by_tag_name("p")
