from page.create_order_page import CreateOrderPage
from common.swipe_option import SwipeOption
import time

class CreateOrderHandle:

    def __init__(self, driver, path):

        self.handle = CreateOrderPage(driver, path)
        self.driver = driver
        self.path = path

    def click_order(self):
        self.handle.order().click()

    def click_offline_order(self):
        self.handle.offline_order().click()

    def click_new_order(self):
        self.handle.new_order().click()

    def send_cust_phone(self, phone):
        self.handle.cust_phone().send_keys(phone)

    def send_cust_name(self, name):
        self.handle.cust_name().send_keys(name)

    def click_series(self):
        self.handle.series().click()

    def select_option(self, option_name):
        """
        根据下拉选项，选择预期结果
        :param name: 下拉选项名称
        :return:
        """
        view = self.handle.option_view()
        SwipeOption(self.driver, self.path).swipe(view,option_name)

    def click_confirm(self):
        self.handle.ok().click()

    def click_merket(self):
        self.handle.market().click()

    def click_vehicle_color(self):
        self.handle.vehicle_color().click()

    def click_inner_color(self):
        self.handle.inner_color().click()

    def click_exchange(self):
        self.handle.exchange().click()

    def send_deposit(self,price):
        SwipeOption(self.driver, self.path).swipe_screen()
        time.sleep(1)
        self.handle.deposit().send_keys(price)

    def click_payments(self):
        self.handle.payments().click()

    def send_mark(self,content):
        self.handle.mark().send_keys(content)

    def click_button(self):
        self.handle.submit_button().click()