import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("******************************** Test_002_DDT *********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of raws:", self.rows)
        lst_status = []
        for r in range(2, self.rows+1):   #self.row yazsak son satırı almayacagı icin +1
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.home_page.elementvisible()
            self.home_page.clickmyaccount()
            self.home_page.elementvisible2()
            self.home_page.clickloginbutton()
            self.login_page.elementvisible()
            self.login_page.setEmail(self.user)
            self.login_page.clickLogin()
            self.login_page.setPassword(self.password)
            self.login_page.clickLogin2()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Türkiye'nin En Büyük Online Alışveriş Sitesi Hepsiburada.com"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    lst_status.append("Pass")
                    self.driver.save_screenshot(".\\Screenshots\\" + "success_test_login_dtt.png")
                    self.home_page.clickmyaccount()
                    self.home_page.logout()
                elif self.exp == "Fail":
                    self.logger.info("**Failed**")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Failed**")
                    lst_status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\" + "failed_test_login_dtt.png")
                    self.driver.back()
                elif self.exp == "Fail":
                    self.logger.info("**Passed**")
                    lst_status.append("Pass")
                    self.driver.back()
                    self.driver.back()

        if "Fail" not in lst_status:
            self.logger.info("Login DDT passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Failed DDT")
            self.driver.quit()
            assert False
