from selenium.webdriver.common.by import By

class ProductElements:

    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-name h1")

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-31")
    ADD_TO_WISHLIST_BUTTON = (
        By.CSS_SELECTOR,
        "input.button-2.add-to-wishlist-button"
    )
    ADD_TO_COMPARE_BUTTON = (
        By.CSS_SELECTOR,
        "input[value='Add to compare list']"
    )
    CART_QTY = (By.CSS_SELECTOR, ".cart-qty")
    WISHLIST_QTY = (By.CSS_SELECTOR, ".wishlist-qty")