from common.get_element import GetElement


class LoginPage:

    def __init__(self,driver,path):
        self.getElement = GetElement(driver,path)

    def get_username(self):
        return self.getElement.get_element("login","account")

    def get_pwd(self):
        return self.getElement.get_element("login","password")

    def get_login_button(self):
        return self.getElement.get_element("login","login_button")

    def avar(self):
        return self.getElement.get_element("login","avar")

    def notice(self):
        return self.getElement.get_element("login","notice")

