# -*- coding: utf-8  -*-
# @File     : loginPage.py
# @author   : Jerry
# @datetime : 2022/3/15 19:14
# @software : PyCharm

from day6.初级版本.myDriver import Driver

class LoginPage:
    def __init__(self):
        #创建driver对象
        self.driver = Driver.getDriver()

        #用户名输入框
    def usernameBox(self):
        return self.driver.find_element_by_name("username")

        #密码输入框
    def pwdBox(self):
        return self.driver.find_element_by_name("password")

        #登录按钮
    def loginButton(self):
        return self.driver.find_element_by_css_selector("button.btn")

#抽离出页面动作类，继承相应的页面类
class LoginPageAction(LoginPage):
    def login(self):
        """登录系统"""
        self.usernameBox().send_keys("libai")
        self.pwdBox().send_keys("opmsopms123")
        self.loginButton().click()

if __name__ == '__main__':
    lp = LoginPageAction()
    lp.login()
