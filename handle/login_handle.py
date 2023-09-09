from page.login_page import LoginPage


class LoginHandle:

    def __init__(self,driver,path):
        self.handle = LoginPage(driver,path)

    def input_username(self,username):
        self.handle.get_username().send_keys(username)

    def input_pwd(self,pwd):
        self.handle.get_pwd().send_keys(pwd)

    def click_button(self):
        self.handle.get_login_button().click()

    def click_avar(self):
        self.handle.avar().click()

    def click_notice(self):
        self.handle.notice().click()