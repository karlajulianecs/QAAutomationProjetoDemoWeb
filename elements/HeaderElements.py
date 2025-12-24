from selenium.webdriver.common.by import By

class HeaderElements:
    CART_LINK = (By.ID, "topcartlink")
    CART_QTY = (By.CSS_SELECTOR, ".cart-qty")
    FLYOUT_CART = (By.ID, "flyout-cart")