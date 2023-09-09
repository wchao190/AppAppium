from appium import webdriver
from common.appium_cmd import AppiumCmd

class BaseDriver:

    def __init__(self):
        self.appium_cmd =  AppiumCmd()

    def android_driver(self,i):
        device = self.appium_cmd.get_value("appium_cmd_"+ str(i),"device")
        port = self.appium_cmd.get_value("appium_cmd_"+ str(i),"port")

        self.profile = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": device,
            "automationName": "UiAutomator2",
            "appPackage": "",
            "appActivity": "",
            "newCommandTimeout":"120"
        }

        driver = webdriver.Remote("http://127.0.0.1:"+ str(port) +"/wd/hub",self.profile)
        return driver
