import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from udemyframeworkcode2.Utility.Baseclass import Baseclass

from udemyframeworkcode2.pageobjects.homepage import homepage1
from udemyframeworkcode2.pageobjects.reginop import nopregipagesitemap
from udemyframeworkcode2.testdata.Testdata import testdata


class nopdemo1(Baseclass):

    def test_nop1(self):
        home=homepage1(self.driver)
        self.actionchains().move_to_element(home.computers).move_to_element(home.desktops).click().perform()
        log=self.test_loggingDemo()
        log.INFO("its desktops details")
        wish=nopregipagesitemap.sitemapclick().click()
        log.INFO("its sitemap details")

# its take the datafrom testdata in dict format we given
@pytest.fixture(params=testdata.test_dataforload)
def dataload(request):
    return request.param

#its take from the the excel sheet
#@pytest.fixture(params=testdata.gettestdata("testcasename"))
# def dataload(request):
#     return request.param








