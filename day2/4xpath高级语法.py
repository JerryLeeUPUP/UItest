# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 4xpath高级语法.py
# @ide     : PyCharm
# @time    : 2020/10/26 21:05
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

ele = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span[1]/input")
ele.send_keys("selenium")

# 当我们使用分步骤定位的时候，在 xpath里边有一个易错点
# 父元素.寻找，所写的表达式必须以点开头
ele = driver.find_element_by_xpath("//div/ol/li")
# 根据父元素定位子元素, 开头必须以点开始
ele1 = ele.find_element_by_xpath("./span/a")
# 如果不用点，那就会从这个文档开始找，即使你前边用了父元素也不行

