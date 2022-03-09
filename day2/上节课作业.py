# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 上节课作业.py
# @ide     : PyCharm
# @time    : 2020/10/26 21:32
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("https://m.weibo.cn/")
# 隐式等待
driver.implicitly_wait(10)

# 点击大家都在搜
driver.find_element_by_xpath("//div[@class=\"m-text-cut\"]").click()

# 点击微博热搜榜
driver.find_element_by_xpath("//div[@id=\"app\"]/div[1]/div[1]/div[2]//div[@class=\"card-main\"]/div[8]").click()

# 匹配到最外层的大标签
hotDivSli = driver.find_element_by_xpath("//div[@id]/div[1]/div[2]/div[3]/div/div")

# 从hotDivSli 中找到每一行热搜标签，存到列表
hotSli = hotDivSli.find_elements_by_xpath("./div")
# 迭代 hotSli 中的每一个元素
for hotDiv in hotSli:
    # 判断这一行热搜存不存在
    imgSli = hotDiv.find_elements_by_xpath(".//span[@class=\"m-link-icon\"]/img")
    if imgSli:
        # 获取到 img 标签的src属性
        srcLink = imgSli[0].get_attribute("src")
        # 判断图片标签的类型是什么
        if "hot" in srcLink:
            hotType = "热"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]")
            print("{}: {}".format(hotType, hotText.text))
        elif "new" in srcLink:
            hotType = "新"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]")
            print("{}: {}".format(hotType, hotText.text))
