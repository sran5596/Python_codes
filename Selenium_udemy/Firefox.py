from selenium import webdriver
from selenium.webdriver.chrome.service import Service
obj=Service("D:\drivers\geckodriver.exe")
driver=webdriver.Firefox(service=obj)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
print(driver.current_url)
print(driver.title)
driver.get("https://www.udemy.com/")
print(driver.title)
driver.implicitly_wait(10)
driver.back()
driver.forward()
driver.close