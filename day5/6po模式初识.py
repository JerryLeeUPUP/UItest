# -*- coding: utf-8  -*-
# @File     : 6po模式初识.py
# @author   : Jerry
# @datetime : 2022/3/15 11:46
# @software : PyCharm
from selenium import webdriver

class loginPage:
    def __init__(self,path):
        #创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #访问网址
        self.driver.get(path)
        #封装用户名输入框
        self.usernameBox = self.driver.find_element_by_name("username")
        #封装密码输入框
        self.passwordBox = self.driver.find_element_by_name("password")
        #封装登录按钮
        self.loginButtonBox = self.driver.find_element_by_name("button")

#抽离出页面动作类，继承对应的页面类
class loginPageAction(loginPage):
    def login(self):
        self.usernameBox.send_keys("libai")
        self.passwordBox.send_keys("123456")
        self.loginButtonBox.click()

if __name__ == '__main__':
    Ip = loginPageAction("XXXX")
    Ip.login()