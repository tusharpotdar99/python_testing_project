import time

from selenium.webdriver.common.by import By

from pages.login_page_adv import LoginPageAdv
from pages.login_page import LoginPage
from utilities import config_reader
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger

def test_valid_login(driver):
    logger = get_logger()
    logger.info("Opening Login page")
    login_page = LoginPage(driver)
    login_page.click_my_account()
    logger.info("Navigating My account menu")
    login_page.click_login()
    logger.info("clicking login option")
    login_page.login_account(ConfigReader.get_username(),ConfigReader.get_password())
    time.sleep(3)
    logger.info("Entering valid details and clicking on login button")
    driver.save_screenshot("screenshots/login_success.png")
    assert login_page.is_my_account_label_displayed()
    logger.info("verifying login success")

def test_invalid_login(driver):
    logger = get_logger()
    logger.info("Opening Login page")
    login_page = LoginPage(driver)
    login_page.click_my_account()
    logger.info("Navigating My account menu")
    login_page.click_login()
    logger.info("clicking login option")
    login_page.login_account("tusharpotdar99@gmail.com","TushOC@199")
    time.sleep(3)
    alert_text = login_page.get_alert_text()
    print(alert_text)
    logger.info("Entering invalid details and clicking on login button")
    driver.save_screenshot("screenshots/login_failed.png")
    assert "Warning" in alert_text
    logger.info("verifying login failed and warning")


def test_valid_login_adv(driver):
    logger = get_logger()
    logger.info("Opening Login page")
    login_page_adv = LoginPageAdv(driver)

    logger.info("entering valid details and clicking on login button")
    login_page_adv.login_adv_method("tusharpotdar99@gmail.com","TushOC@1999")

    driver.save_screenshot("screenshots/login_success_adv.png")

    assert login_page_adv.verify_login()
    logger.info("verifying login success")



def test_invalid_login_adv(driver):
    logger = get_logger()
    login_page_adv = LoginPageAdv(driver)
    logger.info("entering invalid details and clicking on login button")

    login_page_adv.login_adv_method("tusharpotdar99@gmail.com","TushOC@19")
    driver.save_screenshot("screenshots/login_failed_adv.png")

    assert login_page_adv.verify_error_alert()
    logger.info("verifying login failed and warning")


