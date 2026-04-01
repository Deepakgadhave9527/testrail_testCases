import pytest
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("testuser")
    login_page.enter_password("Password123")
    login_page.click_login_button()
    login_page.verify_dashboard_page_loaded()
