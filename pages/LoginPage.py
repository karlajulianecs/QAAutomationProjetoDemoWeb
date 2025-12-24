from pages.BasePage import BasePage
from elements.LoginElements import LoginElements

class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://demowebshop.tricentis.com/login")

    def login(self, email, password):
        self.type(LoginElements.EMAIL, email)
        self.type(LoginElements.PASSWORD, password)
        self.click(LoginElements.LOGIN_BUTTON)