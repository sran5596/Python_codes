from selenium import webdriver
from selenium.webdriver.common.by import By

from udemyframeworkcode2.pageobjects.reginop import nopregipagesitemap


class homepage1:
    registerbutton=(By.XPATH,"//a[@class='ico-register']")
    computers=(By.XPATH,"//a[normalize-space()='Computers']")
    desktops=(By.XPATH,"//a[normalize-space()='Desktops']")

    def __init__(self,driver):
        self.driver=driver

    def computersclick(self):
        return self.driver.find_element(*homepage1.computers)
    def desktops(self):
        return self.driver.find_element(*homepage1.desktops)

    def nopregiclick(self):
        self.driver.find_element(*homepage1.registerbutton).click()
        sitemap=nopregipagesitemap(self.driver)

