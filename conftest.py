import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart/")
    yield driver
    driver.quit()