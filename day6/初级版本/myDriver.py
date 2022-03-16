# -*- coding: utf-8  -*-
# @File     : myDriver.py
# @author   : Jerry
# @datetime : 2022/3/15 19:12
# @software : PyCharm
from selenium import webdriver
from day6.初级版本.mySettings import driverPath

class Driver:
    """浏览器驱动的工具类"""
    #初始化为空
    driver = None

    @classmethod #该修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象等
    def getDriver(cls,browser_name = "Chrome"):
        """
        获取浏览器驱动对象
        :return:
        """
        #如果为空，则需要创建
        if cls.driver is None:
            if browser_name == "Chrome":
                #cls.driver = webdriver.Chrome(driverPath[browser_name])  #浏览器驱动有环境变量就不需要传这个参数
                cls.driver = webdriver.Chrome()
            elif browser_name == "Firefox":
                cls.driver = webdriver.Firefox(driverPath[browser_name])
            #。。。省略其他浏览器类型
            else:
                raise ("找不到浏览器，请检查配置或传参")

            #最大化窗口
            cls.driver.maximize_window()
            #访问网址
            cls.driver.get("http://127.0.0.1:8088/")
        #print(cls.driver)
        return cls.driver

if __name__ == '__main__':
    Driver.getDriver()