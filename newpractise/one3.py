from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.XPATH,"//*[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
error=driver.find_element(By.XPATH,"//*[@id='Email-error']").text
print(error)
