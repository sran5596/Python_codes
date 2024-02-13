
from selenium import webdriver
from selenium.webdriver.common.by import By
class admin:
    admin=(By.XPATH,"//a[@class='oxd-main-menu-item active']")
    org=(By.XPATH, "//a[normalize-space()='Locations']")

    def __init__(self,driver):
        self.driver=driver


    def adminclick(self):
        return self.driver.find_element(*admin.admin)

    def mouseover(self):
        return self.driver.find_element(*admin.org)