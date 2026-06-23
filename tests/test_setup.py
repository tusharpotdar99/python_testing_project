import time

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    yield driver
    driver.quit()

def test_title(driver):
    print(driver.title)
    assert "Your Store" in driver.title