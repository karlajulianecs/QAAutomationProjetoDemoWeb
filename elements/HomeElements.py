from selenium.webdriver.common.by import By

class HomeElements:
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Search']")
    LAPTOP_PRODUCT = (By.LINK_TEXT, "14.1-inch Laptop")