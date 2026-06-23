import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utilities.config_reader import ConfigReader

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(
    #     service=Service(ChromeDriverManager().install())
    # )
    driver.get(ConfigReader.get_url())
    yield driver
    driver.quit()