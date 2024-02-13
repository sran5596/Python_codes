from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from udemyframeworkcode2 import testdata
from udemyframeworkcode2.Utility.Baseclass import Baseclass
from udemyframeworkcode2.pageobjects.homepage import homepage1
import pytest
from udemyframeworkcode2.testdata.Testdata import testdata



class test1(Baseclass):

    def test_fbe2e(self):
        register=homepage1(self.driver)
        register.clickfname().send_keys("firstname")
        register.clicklname().send_keys("lastname")
        register.clickemail().send_keys("email")
        register.clickpws().send_keys("password")
        self.selectofelement(register.day,"5").click()
        self.selectofelement(register.month,"7").click()
        self.selectofelement(register.yrs,"2022").click()
        register.clickgender().send_keys("Male").click()
        log=self.test_loggingDeme()
        log.INFO("register page all taken properly")

#below code is the datataken form the excel sheet in Baseclass
@pytest.fixture(params=testdata.gettestdata("testcasename")) #in excel give the data="testcase2" like that
def dataload(request):
    return request.param

#its directly taje data from the class.variable needed on Baseclass
# @pytest.fixture(params=testdata.test_dataforload)
# def dataload(request):
#     return request.param