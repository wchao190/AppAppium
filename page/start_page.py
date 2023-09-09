from common.get_element import GetElement

class StartPage:

    def __init__(self,driver,path):
        self.getElement = GetElement(driver,path)

    def get_allow(self):
        return self.getElement.get_element("login","allow")