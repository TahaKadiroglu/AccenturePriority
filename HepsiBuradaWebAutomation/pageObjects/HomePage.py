from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    button_myaccount_id = "myAccount"
    button_login_id = "login"
    cikisyap_xpath = "//*[@href='https://www.hepsiburada.com/uyelik/cikis?ReturnUrl=https%3A%2F%2Fwww.hepsiburada.com%2F']"

    def __init__(self, driver):
        self.driver = driver

    def clickmyaccount(self):
        self.driver.find_element("id", self.button_myaccount_id).click()

    def clickloginbutton(self):
        self.driver.find_element("id", self.button_login_id).click()

    def elementvisible(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.button_myaccount_id)))

    def elementvisible2(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.button_login_id)))

    def logout(self):
        self.driver.find_element("xpath", self.cikisyap_xpath).click()
