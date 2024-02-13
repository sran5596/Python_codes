from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("s.raveendra7416@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("sraveendra009403@@")
driver.find_element(By.XPATH,"//button[@id='loginbutton']").click()
