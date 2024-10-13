import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="module")
def web_driver_creation():
    driver: WebDriver = webdriver.Chrome()

    yield driver

    driver.quit()