import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_successful_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("testuser")
        login_page.enter_password("Password123")
        login_page.click_login()
        assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully"

    def test_invalid_email_format(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("invalidemail")
        login_page.enter_password("Password123")
        login_page.click_login()
        error_message = driver.find_element_by_css_selector(".error").text
        assert error_message == "Please enter a valid email address"

    def test_empty_password(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("testuser")
        login_page.enter_password("")
        login_page.click_login()
        error_message = driver.find_element_by_css_selector(".error").text
        assert error_message == "Password cannot be empty"
