from page.start_page import StartPage
from selenium.webdriver.support import expected_conditions as EC
import time

from common.operate_ini import OperateIni

class StartHandle:

    def __init__(self,driver,path):
        self.handle = StartPage(driver,path)
        self.login_ini = OperateIni(path)

    def click_allow(self):
        info = self.login_ini.get_ini("login","allow")
        allow = (info.split(">")[0],info.split(">")[1])
        result1 = EC.presence_of_element_located(allow)
        if result1:
            self.handle.get_allow().click()
        time.sleep(1)