import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from udemyframeworkcode.Baseclass_for_usefixture_statement import usefixture
from udemyframeworkcode.BaseClass_logging_code import Baseclass_logging
from udemyframeworkcode.loginpage import pagelogin
from udemyframeworkcode.adminhavepage import admin




# @pytest.mark.usefixtures("setup")
class Totalcode(usefixture,Baseclass_logging):
    def test_e2edemo1(self):

        loginpage=pagelogin.password(self.driver) #it for login page object
        # adminbutton=admin.adminclick(self.driver) # admin page dashboard
        adminbutton=loginpage.button()

        # mywait=WebDriverWait(self.driver,10)
        # mywait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")))
        # mywait.send_keys("Admin")
        self.test_e2edemo1().send_keys("Admin") # its for WebdriverWait total optiome here imported on usefixturepage
        # self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        loginpage.passwordfield.send_keys("admin123")
        # self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        # loginpage.loginbutton.click() #its not required its done on the loginpage itself

        actual_title=self.driver.title
        expected_title="OrangeHRM"
        if actual_title==expected_title:
            print("pass")
        else:
            print("fail")
        assert actual_title!=expected_title
        log=self.test_loggingDemo()
        log.info("its info details related")
        act=webdriver.ActionChains(self.driver)
        # self.driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
        adminbutton.adminclick.click()
        # act.move_to_element(By.XPATH,"//a[normalize-space()='Locations']").click().perform()
        act.move_to_element(adminbutton.mouseover()).click().perform()




