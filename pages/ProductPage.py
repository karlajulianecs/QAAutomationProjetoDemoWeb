from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.BasePage import BasePage
from elements.ProductElements import ProductElements


class ProductPage(BasePage):

    def wait_product_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(
                ProductElements.PRODUCT_TITLE
            )
        )

    def add_to_cart(self):
        self.wait_product_loaded()

        self.click(ProductElements.ADD_TO_CART_BUTTON)

        self.wait.until(
            EC.text_to_be_present_in_element(
                ProductElements.CART_QTY, "(1)"
            )
        )

    def add_to_wishlist(self):
        self.wait_product_loaded()

        button = self.wait.until(
            EC.presence_of_element_located(
                ProductElements.ADD_TO_WISHLIST_BUTTON
            )
        )

        # Garantir posição na viewport
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        ActionChains(self.driver).move_to_element(button).pause(0.2).click().perform()

        self.wait.until(
            EC.text_to_be_present_in_element(
                ProductElements.WISHLIST_QTY, "(1)"
            )
        )

    def add_to_compare(self):
        self.wait_product_loaded()

        self.scroll_into_view(ProductElements.ADD_TO_COMPARE_BUTTON)

        self.click(ProductElements.ADD_TO_COMPARE_BUTTON)