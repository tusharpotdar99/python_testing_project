from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageAdv(BasePage):

    my_account = (By.XPATH , "//span[normalize-space()='My Account']")
    login = (By.XPATH,"//a[normalize-space()='Login']")

    username = (By.XPATH,"//input[@id='input-email']")
    password = (By.XPATH,"//input[@id='input-password']")
    login_button = (By.XPATH,"//button[normalize-space()='Login']")
    my_account_label = (By.XPATH,"//h1[normalize-space()='My Account']")
    alert_path = (By.XPATH, "//div[@id='alert']//div[contains(@class,'alert')]")
    expected = "Warning: No match for E-Mail Address and/or Password."
    close_btn = (By.XPATH,"//div[@id='alert']//div[contains(@class,'alert')]//button")

    def login_adv_method(self, username, password):

        self.click(self.my_account)
        self.click(self.login)
        self.enter_text(self.username, username)
        self.enter_text(self.password, password)
        self.click(self.login_button)

    def verify_login(self):
        self.driver.save_screenshot("screenshots/verify_login.png")
        return self.is_displayed(self.my_account_label)

    def verify_error_alert(self):
        self.driver.save_screenshot("screenshots/error_alert.png")
        return self.get_text(self.alert_path)
