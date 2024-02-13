from selenium import webdriver
from selenium.webdriver.common.by import By
class dashboardpage:
    catalog=(By.LINK_TEXT,"Catalog")
    products=(By.LINK_TEXT,"Products")
    def __init__(self,driver):
        self.driver=driver

    def catalog(self):
        return self.driver.find_element(*dashboardpage.catalog)

    def products(self):
        return self.driver.find_element(*dashboardpage.products)


