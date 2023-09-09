#conding=utf-8
import platform

from common.server import Server
import unittest,time
from common.ParameterizedTestCase import ParameterizedTestCase
from case.test1 import Login
import os
import multiprocessing
import HTMLTestRunner_cn
from common.appium_cmd import AppiumCmd

class Run:

    def appium_init(self):
        server  = Server()
        server.start_thead()

    def get_suite(self,i):
        suite = unittest.TestSuite()
        suite.addTest(ParameterizedTestCase.parameterized(Login, args=i))

        report_path = os.path.join(os.path.dirname(os.getcwd()), "report",AppiumCmd().get_value("appium_cmd_" + str(i), "model") + ".html")
        fp = open(report_path, "wb")

        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title="i营销APP测试报告", description="自动化测试")
        runner.run(suite)

    def count_cmd(self):
        return AppiumCmd().count_cmd()

if __name__ == '__main__':

    run = Run()
    run.appium_init()

    driver = []
    count = run.count_cmd()

    for  i in range(count):
        p = multiprocessing.Process(target= run.get_suite, args=(i,))
        driver.append(p)

    for proce in driver:
        proce.start()
        #print(proce.pid)
