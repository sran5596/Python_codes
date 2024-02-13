from selenium import webdriver
from selenium.webdriver.common.by import By
from udemyframeworkcode.adminhavepage import admin
class pagelogin:

    passwordfield=(By.XPATH,"//input[@name='password']")
    loginbutton=(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")

    def __init__(self,driver): # its establish the relation ship between the actual test class to login oage class
        self.driver=driver

    def password(self): #its for the passwrd field
        return self.driver.find_element(*pagelogin.passwordfield)

    def button(self): #its for  the logib button
        # return self.driver.find_element(*pagelogin.loginbutton) # its first one here optimezed
        self.driver.find_element(*pagelogin.loginbutton).click()
        adminbutton = admin.adminclick(self.driver)
        return adminbutton

