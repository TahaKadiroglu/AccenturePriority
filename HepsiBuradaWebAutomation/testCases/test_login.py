import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username1 = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("******************************** Test_001_Login *********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.elementvisible()
        home_page.clickmyaccount()
        home_page.elementvisible2()
        home_page.clickloginbutton()
        login_page.elementvisible()
        login_page.setEmail(self.username1)
        login_page.clickLogin()
        login_page.setPassword(self.password)
        login_page.clickLogin2()
        self.logger.info("*************************Login Test Succesful************************")
        time.sleep(5)
        pagetitle = self.driver.title
        if pagetitle == "Türkiye'nin En Büyük Online Alışveriş Sitesi Hepsiburada.com":
            self.driver.save_screenshot(".\\Screenshots\\" + "success_test_login.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "failed_test_login.png")
            assert False
        self.driver.quit()

