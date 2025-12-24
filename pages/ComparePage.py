from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from elements.CompareElements import CompareElements


class ComparePage(BasePage):

    def open(self):
        self.driver.get("https://demowebshop.tricentis.com/compareproducts")

    def has_products(self) -> bool:
        return self.is_visible(CompareElements.COMPARE_TABLE)