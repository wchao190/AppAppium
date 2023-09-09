from handle.start_handle import StartHandle


class StartBusiness:

    def __init__(self,driver,path):
        self.business = StartHandle(driver,path)

    def click_allow(self):
        self.business.click_allow()
        self.business.click_allow()
