import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
print(driver.title)
driver.close()
