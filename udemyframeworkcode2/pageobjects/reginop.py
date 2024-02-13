from selenium import webdriver
from selenium.webdriver.common.by import By

from udemyframeworkcode2.pageobjects.nopwishlist import nopwishlist


class nopregipagesitemap:

    sitemap=(By.XPATH,"//a[normalize-space()='Sitemap']")

    def __init__(self,driver):
        self.driver=driver

    def sitemapclick(self):
         self.driver.find_element(*nopregipagesitemap.sitemap).click()
         wish=nopwishlist(self.driver)
