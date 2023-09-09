from common.get_element import GetElement

class CreateOrderPage:

    def __init__(self,driver,path):
        self.get_element = GetElement(driver,path)

    def order(self):
        return self.get_element.get_element("order","order")

    def offline_order(self):
        return self.get_element.get_element("order","offline")

    def new_order(self):
        return self.get_element.get_element("order","new_order")

    def cust_phone(self):
        return self.get_element.get_element("order","cust_phone")

    def cust_name(self):
        return self.get_element.get_element("order","cust_name")

    def series(self):
        return self.get_element.get_element("order","series")

    def option_list(self):
        return self.get_element.get_element("order","option_list")

    def option_view(self):
        return self.get_element.get_element("order","option_view")

    def ok(self):
        return self.get_element.get_element("order","ok")

    def market(self):
        return self.get_element.get_element("order","market")

    def vehicle_color(self):
        return self.get_element.get_element("order","vehicle_color")

    def inner_color(self):
        return self.get_element.get_element("order","inner_color")


    def exchange(self):
        """
        增换购类型
        :return:
        """
        return self.get_element.get_element("order","exchange")

    def deposit(self):
        """
        定金金额
        :return:
        """
        return self.get_element.get_element("order","deposit")

    def payments(self):
        """
        支付方式
        :return:
        """
        return self.get_element.get_element("order","payments")

    def mark(self):
        return self.get_element.get_element("order","mark")

    def submit_button(self):
        return self.get_element.get_element("order","submit_order")
