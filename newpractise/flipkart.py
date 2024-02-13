from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
obj=Service("D:\drivers/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
    #return driver
#driver=test_firstone()
driver.get("https://www.flipkart.com/")
print(driver.title)