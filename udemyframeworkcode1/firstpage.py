from selenium import webdriver
from selenium.webdriver.common.by import By
from udemyframeworkcode1.dashboardpage import dashboardpage

class loginpage:
    email=(By.XPATH,"//input[@id='Email']")
    paw=(By.XPATH,"//input[@id='Password']")
    button=(By.XPATH, "//button[@type='submit']")

    def __init__(self,driver):
        self.driver=driver

    def email(self):
        return self.driver.find_element(*loginpage.email)

    def password(self):
        return self.driver.find_element(*loginpage.paw)

    def loginbutton(self):
        self.driver.find_element(*loginpage.button).click()
        dashboardpage=dashboardpage(self.driver)
        return dashboardpage


