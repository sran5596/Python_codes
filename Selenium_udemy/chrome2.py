import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window
driver.get("https://www.flipkart.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.udemy.com/")
print(driver.title)
driver.back()
driver.forward()
time.sleep(5)
driver.close()