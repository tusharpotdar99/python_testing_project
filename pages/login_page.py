from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:

    my_account = (By.XPATH , "//span[normalize-space()='My Account']")
    login = (By.XPATH,"//a[normalize-space()='Login']")

    username = (By.XPATH,"//input[@id='input-email']")
    password = (By.XPATH,"//input[@id='input-password']")
    login_button = (By.XPATH,"//button[normalize-space()='Login']")
    my_account_label = (By.XPATH,"//h1[normalize-space()='My Account']")
    alert_path = (By.XPATH, "//div[@id='alert']//div[contains(@class,'alert')]")
    expected = "Warning: No match for E-Mail Address and/or Password."
    close_btn = (By.XPATH,"//div[@id='alert']//div[contains(@class,'alert')]//button")

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(*self.my_account).click()

    def click_login(self):
        self.driver.find_element(*self.login).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login_account(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_my_account_label_displayed(self):
        return self.driver.find_element(*self.my_account_label).is_displayed()

    def get_alert_text(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located(self.alert_path))
        # alert = self.driver.find_element(*self.alert_path)
        # alert = driver.find_element(By.XPATH, "//div[contains(text(),'Warning')]")
        text = alert.text
        self.driver.find_element(*self.close_btn).click()
        return text

