from common.get_element import GetElement

class LogoutPage:

    def __init__(self,driver,path):
        self.get_element = GetElement(driver,path)

    def apply(self):
        return self.get_element.get_element("logout","apply")

    def setting(self):
        return self.get_element.get_element("logout","setting")

    def close_button(self):
        return self.get_element.get_element("logout","logout_button")

    def ok(self):
        return self.get_element.get_element("logout","ok")