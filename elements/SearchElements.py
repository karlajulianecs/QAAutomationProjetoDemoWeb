from selenium.webdriver.common.by import By


class SearchElements:
    SORT_DROPDOWN = (By.ID, "products-orderby")
    PRODUCT_LIST = (By.CLASS_NAME, "product-item")
   # PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")