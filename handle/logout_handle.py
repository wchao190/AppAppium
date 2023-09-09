from page.logout_page import LogoutPage


class LogoutHandle:

    def __init__(self,driver,path):

        self.logout_handle = LogoutPage(driver,path)

    def click_apply(self):
        self.logout_handle.apply().click()

    def click_setting(self):
        self.logout_handle.setting().click()

    def click_button(self):
        self.logout_handle.close_button().click()

    def click_ok(self):
        self.logout_handle.ok().click()