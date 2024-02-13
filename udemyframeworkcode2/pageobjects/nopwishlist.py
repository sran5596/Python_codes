from selenium import webdriver
from selenium.webdriver.common.by import By
class nopwishlist:
    wishlistbutton=(By.XPATH,"//a[@class='wishlist-wishlist']")

    def __init__(self,driver):
        self.driver=driver

    def wishlistclick(self):
        return self.driver.find_element(*nopwishlist.wishlistbutton)
