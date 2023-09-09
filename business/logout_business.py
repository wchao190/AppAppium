from handle.logout_handle import LogoutHandle

class LogoutBusiness:

    def __init__(self,driver,path):
        self.logout_business = LogoutHandle(driver,path)

    def exit_iyx(self):
        self.logout_business.click_apply()
        # self.logout_business.click_setting()
        # self.logout_business.click_button()
        # self.logout_business.click_ok()