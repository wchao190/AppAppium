from handle.create_order_handle import CreateOrderHandle
import time
class CreateOrderBusiness:

    def __init__(self,driver,path):
        self.order_business = CreateOrderHandle(driver,path)
        self.driver = driver

    def create_offline_order(self,phone,name,serie_name,market_name,vehicle_color,inner_color,exchange_name,price,pay_method,content="App自动化测试定金订单"):

        # 定金订单
        self.order_business.click_order()

        # 选择线下订单
        self.order_business.click_offline_order()
        time.sleep(3)

        self.order_business.click_new_order()
        time.sleep(1)

        self.order_business.send_cust_phone(phone)
        self.order_business.send_cust_name(name)

        # 点击车系下拉选项，并选择车系
        self.order_business.click_series()
        self.order_business.select_option(serie_name)
        self.order_business.click_confirm()
        time.sleep(0.5)

        # 点击市场下拉选项，并选择车系
        self.order_business.click_merket()
        self.order_business.select_option(market_name)
        self.order_business.click_confirm()

        # 点击车辆颜色，并选择颜色
        self.order_business.click_vehicle_color()
        self.order_business.select_option(vehicle_color)
        self.order_business.click_confirm()

        # 点击车辆内饰，并选择颜色
        self.order_business.click_inner_color()
        self.order_business.select_option(inner_color)
        self.order_business.click_confirm()

        # 点击增换购类型
        self.order_business.click_exchange()
        self.order_business.select_option(exchange_name)
        self.order_business.click_confirm()
        time.sleep(0.5)

        # 定金
        self.order_business.send_deposit(price)

        # 选择支付方式
        self.order_business.click_payments()
        self.order_business.select_option(pay_method)
        self.order_business.click_confirm()

        self.order_business.send_mark(content)

        self.order_business.click_button()