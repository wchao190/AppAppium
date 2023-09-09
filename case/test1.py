# encoding=utf-8

import os
import platform
import chardet
from business.login_business import LoginBusiness
from business.logout_business import LogoutBusiness
from business.create_order_business import CreateOrderBusiness

from base.base_driver import BaseDriver

from common.ParameterizedTestCase import ParameterizedTestCase

from common.cmd import Cmd
import time


class Login(ParameterizedTestCase):
    def __init__(self, methodName, param):
        """
        :param methodName: 测试用例所在类,传递给父类 ParameterizedTestCase 的初始化函数
        :param param: 设备号,传递给父类 ParameterizedTestCase 的初始化函数,同时本地保存一份，在 serUpClass 中使用
        """
        super(Login, self).__init__(methodName, param)
        global serial
        serial = self.serial_number

    @classmethod
    def setUpClass(cls):
        cls.driver = BaseDriver().android_driver(serial)

        login_ini = os.path.join(os.path.dirname(os.getcwd()), "data\login.ini")
        cls.login = LoginBusiness(cls.driver, login_ini)
        cls.login.login("SQ3776ZTXSGW", "123456")

        # self.login.login("liuke11","123456")

        logout_ini = os.path.join(os.path.dirname(os.getcwd()), "data\logout.ini")
        cls.logout = LogoutBusiness(cls.driver, logout_ini)

        order_ini = os.path.join(os.path.dirname(os.getcwd()), "data\order.ini")
        cls.create_order = CreateOrderBusiness(cls.driver, order_ini)

    def setUp(self):
        # self.driver = BaseDriver().android_driver(self.serial_number)
        # start_bussiness = StartBusiness(self.driver,os.path.join(os.path.dirname(os.getcwd()),"data/login.ini"))
        # start_bussiness.click_allow()
        pass

    def test_1(self):

        self._testMethodName = "i营销线下订单新增"

        self.logout.exit_iyx()
        time.sleep(5)

        self.create_order.create_offline_order("15210361048", "刘支援", "荣威eRX5","PHEV国潮荣麟豪华版","珠光白","浅色","不参加增换购",1000,"全款购车")
        self.driver.save_screenshot( os.path.join(os.path.dirname(os.getcwd()),"report", self._testMethodName + ".png") )

        time.sleep(10)

    def tearDown(self):
        # self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls):
        Cmd().close_appium_server(serial)