from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_successful_login(setup_browser):
    driver = setup_browser
    login_page = LoginPage(driver)

    # Step 1: Navigate to the login page
    login_page.navigate_to_login_page()
    assert driver.current_url == login_page.LOGIN_URL, "Login page URL is incorrect."

    # Step 2: Enter valid username
    login_page.enter_username("testuser")

    # Step 3: Enter valid password
    login_page.enter_password("Password123")

    # Step 4: Click login button
    login_page.click_login_button()

    # Step 5: Verify dashboard page
    WebDriverWait(driver, 10).until(EC.url_to_be("https://practicetestautomation.com/logged-in-successfully"))
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully", "Dashboard URL is incorrect."