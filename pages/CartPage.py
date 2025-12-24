from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from pages.BasePage import BasePage
from elements.CartElements import CartElements


class CartPage(BasePage):

    def open(self):
        self.driver.get("https://demowebshop.tricentis.com/cart")

    def has_products(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(CartElements.CART_TABLE)
            )
            return True
        except TimeoutException:
            return False

    def update_quantity(self, quantity: str):
        if not self.has_products():
            raise AssertionError(
                "Carrinho vazio. Não é possível atualizar quantidade."
            )

        qty_input = self.wait.until(
            EC.visibility_of_element_located(CartElements.QTY_INPUT)
        )
        qty_input.clear()
        qty_input.send_keys(quantity)

        self.click(CartElements.UPDATE_BUTTON)

    def get_quantity(self):
        """Retorna a quantidade atual do produto no carrinho"""
        return self.wait.until(
            EC.visibility_of_element_located(CartElements.QTY_INPUT)
        ).get_attribute("value")

    def remove_product(self):
        if not self.has_products():
            return

        self.click(CartElements.REMOVE_CHECKBOX)
        self.click(CartElements.UPDATE_BUTTON)

    def is_empty(self):
        text = self.wait.until(
            EC.visibility_of_element_located(CartElements.EMPTY_MESSAGE)
        ).text
        return "Your Shopping Cart is empty!" in text

    #ct-007 — Estimar Frete
    def estimate_shipping(self, country: str, zip_code: str):
        """Estima o frete com base no país e CEP"""
        if not self.has_products():
            raise AssertionError(
                "Não é possível estimar frete com carrinho vazio."
            )

        country_select = Select(
            self.wait.until(
                EC.element_to_be_clickable(CartElements.COUNTRY_DROPDOWN)
            )
        )
        country_select.select_by_visible_text(country)

        self.type(CartElements.ZIP_CODE_INPUT, zip_code)
        self.click(CartElements.ESTIMATE_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(CartElements.SHIPPING_RESULT)
        )

    def has_shipping_result(self) -> bool:
        """Verifica se o resultado do frete foi exibido"""
        return self.is_visible(CartElements.SHIPPING_RESULT)