from selenium.webdriver.common.by import By

class LoginPage:
    LOGIN_URL = "https://practicetestautomation.com/practice-test-login"
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()