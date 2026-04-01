import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()