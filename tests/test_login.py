import time

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_valid_login(driver):

    login_page = LoginPage(driver)
    login_page.click_my_account()
    login_page.click_login()

    login_page.login_account("tusharpotdar99@gmail.com","TushOC@1999")
    time.sleep(3)
    assert login_page.is_my_account_label_displayed()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.click_my_account()
    login_page.click_login()
    login_page.login_account("tusharpotdar99@gmail.com","TushOC@199")
    time.sleep(3)
    alert_text = login_page.get_alert_text()
    print(alert_text)
    assert "Warning" in alert_text

