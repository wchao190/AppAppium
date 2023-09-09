import time
from common.get_element import GetElement
from page.create_order_page import CreateOrderPage

class SwipeOption:

    def __init__(self,driver,path):
        self.driver = driver
        self.get_element = GetElement(driver,path)
        self.page = CreateOrderPage(driver,path)

    def swipe(self,element,option_name):
        #ele = self.driver.find_element_by_xpath("//*[@resource-id='app']/android.view.View[3]/android.view.View/android.view.View/android.view.View[3]")
        """
        滑动下拉列表
        :param element: 元素选择框
        :param option_name: 预期选项
        :return:
        """

        # 获取元素起点坐标、尺寸
        location = element.location
        size = element.size
        # 计算元素中心点
        centerx = location['x'] + size['width'] / 2
        centery = location['y'] + size['height'] / 2
        val = self.driver.find_element_by_xpath("//*[@resource-id='app']/android.view.View[3]/android.view.View/android.view.View/android.view.View[3]")
        val_height = val.size['height']

        flag = True
        while flag:
            # list = self.driver.find_elements_by_xpath("//*[@resource-id='app']/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.widget.Button")
            list = self.page.option_list()
            for ele in list:
                if ele.text == option_name:
                    ele.click()
                    flag = False
            else:
                if flag:
                    self.driver.swipe(centerx, centery, centerx, centery - val_height*0.6, 300)
                    time.sleep(0.5)

    def swipe_screen(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        self.driver.swipe(x*0.5, y*0.9, x*0.5, y*0.1,500)