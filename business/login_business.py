from handle.login_handle import LoginHandle
from business.logout_business import LogoutBusiness



class LoginBusiness:

    def __init__(self,driver,path):

        self.business = LoginHandle(driver,path)

    def login(self,username,pwd):
        self.business.input_username(username)
        self.business.input_pwd(pwd)
        self.business.click_button()

        self.business.click_avar()
        self.business.click_notice()