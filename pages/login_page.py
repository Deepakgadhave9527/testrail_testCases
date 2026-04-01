from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    LOGIN_PAGE_URL = "https://practicetestautomation.com/practice-test-login"
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")
    DASHBOARD_URL = "https://practicetestautomation.com/logged-in-successfully"

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_dashboard_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.DASHBOARD_URL))
