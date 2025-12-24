from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.HeaderElements import HeaderElements


class HeaderComponent:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def hover_cart(self):
        cart = self.wait.until(
            EC.visibility_of_element_located(HeaderElements.CART_LINK)
        )
        ActionChains(self.driver).move_to_element(cart).perform()

    def get_cart_quantity(self):
        """Retorna o texto do contador do carrinho, ex: '(1)'"""
        return self.wait.until(
            EC.visibility_of_element_located(HeaderElements.CART_QTY)
        ).text

    def get_flyout_text(self):
        """Retorna o texto do flyout do carrinho após hover"""
        self.hover_cart()
        return self.wait.until(
            EC.visibility_of_element_located(HeaderElements.FLYOUT_CART)
        ).text