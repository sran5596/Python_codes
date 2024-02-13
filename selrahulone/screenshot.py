from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()
def screen_one():
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
driver=screen_one()
driver.get("https://www.foundit.in/")
driver.save_screenshot(location+"\\foundit.png")
driver.quit()
