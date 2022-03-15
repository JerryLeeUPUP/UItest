# -*- coding: utf-8  -*-
# @File     : 4获取登陆后的cookie.py
# @author   : Jerry
# @datetime : 2022/3/14 16:32
# @software : PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint

driver = webdriver.Chrome()
driver.get("https://qa2-www.yunquna.com/")

driver.implicitly_wait(10)
#ele = WebDriverWait(driver, 5, 0.5).until(
#    EC.visibility_of_element_located(
#        (By.CSS_SELECTOR,"img.close-icon")
#    )
#)
driver.maximize_window()
driver.find_element_by_css_selector("img.close-icon").click()
#点击注册/登录按钮
driver.find_element_by_css_selector("div.common-top-bar-info-operate-area").click()

#弹出登录弹框，发现是iframe类型，先找到内嵌页面
ifa = driver.find_element_by_css_selector("iframe.login-fixed-modal-iframe")
#切入内嵌页面
driver.switch_to.frame(ifa)
driver.find_element_by_xpath("//input[@id=\"account\"]").send_keys("info@shippingren.com")
driver.find_element_by_css_selector("#verify_code").send_keys("1111")
driver.find_element_by_css_selector("button.login-button").click()
# 切回主页面
driver.switch_to.default_content()

#获取cookie信息
Ck = driver.get_cookies()
pprint.pprint(Ck)