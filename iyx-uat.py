from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StartApp:

    def __init__(self):
        self.profile = {

            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "automationName": "UiAutomator2",
            "appPackage": "com.saicmotor.joywok.uat",
            "appActivity": "com.dogesoft.joywok.SplashActivity"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.profile)

        phone_allow = ("id","com.android.packageinstaller:id/permission_allow_button")
        result1  = EC.presence_of_element_located(phone_allow)
        if result1:
            self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)

        other_allow = ("id","com.android.packageinstaller:id/permission_allow_button")
        result2 = EC.presence_of_element_located(other_allow)
        if result2:
            self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        time.sleep(2)

    def login(self,username,pwd):
        WebDriverWait(self.driver,15,0.5).until(lambda x : x.find_element_by_id("com.saicmotor.joywok.uat:id/editText_account")).send_keys(username)
        WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element_by_id("com.saicmotor.joywok.uat:id/editText_password")).send_keys(pwd)
        WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element_by_id("com.saicmotor.joywok.uat:id/layout_button_login")).click()
        time.sleep(20)

if __name__ == '__main__':
    s = StartApp()
    s.login("liuke11","123456")