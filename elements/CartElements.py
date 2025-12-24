from selenium.webdriver.common.by import By


class CartElements:
    CART_TABLE = (By.CSS_SELECTOR, ".cart")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, ".order-summary-content")

    REMOVE_CHECKBOX = (By.NAME, "removefromcart")
    UPDATE_BUTTON = (By.NAME, "updatecart")
    QTY_INPUT = (By.CSS_SELECTOR, "input.qty-input")

    COUNTRY_DROPDOWN = (By.ID, "CountryId")
    ZIP_CODE_INPUT = (By.ID, "ZipPostalCode")
    ESTIMATE_BUTTON = (By.NAME, "estimateshipping")
    SHIPPING_RESULT = (By.CSS_SELECTOR, ".shipping-results")