from pages.BasePage import BasePage
from elements.HomeElements import HomeElements


class HomePage(BasePage):

    def open(self):
        self.driver.get("https://demowebshop.tricentis.com/")

    def search_product(self, text):
        self.type(HomeElements.SEARCH_INPUT, text)
        self.click(HomeElements.SEARCH_BUTTON)

    def open_laptop(self):
        self.click(HomeElements.LAPTOP_PRODUCT)