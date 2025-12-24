from selenium.webdriver.common.by import By

class LoginElements:
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")