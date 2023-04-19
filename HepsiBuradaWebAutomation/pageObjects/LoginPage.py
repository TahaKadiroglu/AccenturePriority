from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class LoginPage:
    textbox_email_id = "txtUserName"
    button_login_id = "btnLogin"
    textbox_password_id = "txtPassword"
    button_login_id2 = "btnEmailSelect"
    back_button_xpath = "//*[@viewBox='0 0 18 17']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element("id", self.textbox_email_id).clear()
        self.driver.find_element("id", self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("id", self.button_login_id).click()

    def clickLogin2(self):
        self.driver.find_element("id", self.button_login_id2).click()

    def elementvisible(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.textbox_email_id)))
