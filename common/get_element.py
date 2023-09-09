from common.operate_ini import OperateIni
from selenium.webdriver.support.ui import WebDriverWait

class GetElement:

    def __init__(self,driver,path):

        self.driver = driver
        self.readIni = OperateIni(path)

    def get_element(self,section,key):

        param = self.readIni.get_ini(section,key)

        if param:
            method = param.split(">")[0]
            info = param.split(">")[1]
            if method == "id":
                return WebDriverWait(self.driver,20,1).until(lambda x : x.find_element_by_id(info))
            elif method == "xpath":
                return WebDriverWait(self.driver,20,1).until(lambda x : x.find_element_by_xpath(info))
            elif method == "className":
                return WebDriverWait(self.driver,20,1).until(lambda x : x.find_element_by_class_name(info))
            elif method == "elementsClassName":
                return WebDriverWait(self.driver,20,1).until(lambda x : x.find_elements_by_class_name(info))
            elif method == "uiautomator":
                return WebDriverWait(self.driver,15,1).until(lambda x : x.find_element_by_android_uiautomator(info))
            elif method == "xpaths":
                return WebDriverWait(self.driver, 15, 1).until(lambda x: x.find_elements_by_xpath(info))
        else:
            return "没有获取到"+section+"数据"
