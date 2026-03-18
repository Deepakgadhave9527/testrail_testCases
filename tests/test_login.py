from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
 
 
class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)
 
    # Locators

    USERNAME = (By.CSS_SELECTOR, "#username")

    PASSWORD = (By.CSS_SELECTOR, "#password")

    LOGIN_BTN = (By.CSS_SELECTOR, "#submit")

    HEADER = (By.TAG_NAME, "h1")
 
    # Actions

    def load(self, url):

        self.driver.get(url)

        self.wait.until(EC.presence_of_element_located(self.USERNAME))
 
    def enter_username(self, username):

        self.driver.find_element(*self.USERNAME).send_keys(username)
 
    def enter_password(self, password):

        self.driver.find_element(*self.PASSWORD).send_keys(password)
 
    def click_login(self):

        self.driver.find_element(*self.LOGIN_BTN).click()
 
    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()
 
    def get_header_text(self):

        return self.wait.until(

            EC.presence_of_element_located(self.HEADER)

        ).text
 
    def wait_for_dashboard(self, dashboard_url):

        self.wait.until(EC.url_to_be(dashboard_url))
 