
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
#we pass the u.n and p.w through to url
#syntax=https://username:password@the-internet.herokuapp.com/basic_auth
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
print(driver.find_element(By.XPATH,"//*[@id='content']/div/p").text)
time.sleep(5)
