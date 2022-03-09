# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 上次作业.py
# @ide     : PyCharm
# @time    : 2020/10/30 21:45
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.51job.com/")

# 1、点击高级搜索
driver.find_element_by_css_selector("a.more").click()

# 2输入关键词 python
driver.find_element_by_id("kwdselectid").send_keys("python")

"""
# # 3地区选择杭州
# # 点击地区按钮
# driver.find_element_by_id("work_position_click").click()
# # 取消选中默认城市
# driver.find_element_by_css_selector("#work_position_click_multiple_selected > span").click()
# # 找到杭州地区并点击
# driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
# # 点击确定按钮
# driver.find_element_by_id("work_position_click_bottom_save").click()
"""
# 3地区选择杭州
# 点击地区按钮
driver.find_element_by_id("work_position_click").click()
# 取消选中默认城市
driver.find_element_by_css_selector("#work_position_click_multiple_selected > span").click()
# 点击 HI
driver.find_element_by_css_selector("li#work_position_click_center_left_each_220200").click()
# 点击杭州
driver.find_element_by_id("work_position_click_center_right_list_category_220200_080200").click()
# 点击确定按钮
driver.find_element_by_id("work_position_click_bottom_save").click()

# 4职能选择 计算机软件-》高级软件工程师
# 由于控件遮挡，点击一下空白区域
driver.find_element_by_css_selector("div.rtit.r1").click()
# 点击职能类别选择按钮
driver.find_element_by_id("funtype_click").click()
# 点击后端开发
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
# 点击高级软件工程师
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
# 点击确定按钮
driver.find_element_by_id("funtype_click_bottom_save").click()

# 5工作年限选一到三年
# 点击展开工作年限下拉框
driver.find_element_by_id("workyear_list").click()
# 点击一到三年
driver.find_element_by_css_selector("span[title=\"1-3年\"]").click()

# 6点击搜索，确认搜索职位
driver.find_element_by_css_selector("div.btnbox.p_sou > span.p_but").click()

# 7 获取职位列表并按要求打印
# 获取职位列表
jobEleSli = driver.find_elements_by_css_selector("div.j_joblist > div")

# 获取页数
num = driver.find_element_by_css_selector("div.p_in > span.td:nth-child(1)").text.replace(" ", "", -1).replace("共", "",
                                                                                                               -1).replace(
    "页", "", -1)
for i in range(int(num)):
    for job in jobEleSli:
        # 在一行职位元素中找 span 标签, infoSli--》职位信息存储元素列表
        infoSli = job.find_elements_by_css_selector("span")
        # 获取职位名称
        jobName = infoSli[0].text
        # 公司名称
        cName = job.find_element_by_css_selector("a[title]").text
        # 地区
        cityName = infoSli[3].text.split("|")[0].replace(" ", "", -1)
        # 月薪
        price = infoSli[2].text
        # 日期
        date = infoSli[1].text.replace("发布", "", -1)

        print(" | ".join([jobName, cName, cityName, price, date]))

    if int(num) == 1:
        break
    # 点击翻页按钮
    driver.find_element_by_css_selector("li.bk.next i.e_icons").click()
