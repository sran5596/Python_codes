from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

from udemyframeworkcode1.Baseclass import Baseclass
from udemyframeworkcode1.firstpage import loginpage
from udemyframeworkcode1.BaseClass_logging_code import Baseclass_logging_code
from udemyframeworkcode2.testdata.Testdata import testdata


# @pytest.mark.usefixtures("browsers")
class end2end(Baseclass,Baseclass_logging_code):

    def test_onee2e(self):
        loginpage=loginpage(self.driver)
        dashboardpage=loginpage.loginbutton()

        # self.driver.find_element(By.XPATH,"//input[@id='Email']").clear()
        # self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
        # self.driver.find_element(By.XPATH,"//input[@id='Password']").clear()
        # self.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
        # self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        loginpage.email.clear()
        loginpage.email.send_keys("admin@yourstore.com")
        loginpage.paw.clear()
        loginpage.paw.send_keys("admin")
        loginpage.lohinbutton

        # mywait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='Email']")))
        self.waits("//input[@id='Email']")

        # driver.find_element(By.LINK_TEXT,"Catalog").click()
        # mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"Catalog"))).click()
        self.waits("//p[normalize-space()='Catalog']")
        time.sleep(5)
        # mywait.until(EC.presence_of_element_located(By.XPATH,"//p[normalize-space()='Products']")).click()
        self.waits("//p[normalize-space()='Products']").click()
        # driver.find_element(By.LINK_TEXT,"HP Spectre XT Pro UltraBook")
        log=self.test_loggingDemo()
        log.INFO(self.driver.title)

#below code is the datataken form the excel sheet in Baseclass
@pytest.fixture(params=testdata.gettestdata("testcasename")) # in excel give the data="testcase2" like that
def dataload(request):
    return request.param

#below code for the data take directly we given in dict format
# @pytest.fixture(params=testdata.test_dataforload)
# def dataload(request):
#     return request.param





