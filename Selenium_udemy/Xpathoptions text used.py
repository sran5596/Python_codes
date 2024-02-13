import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(5)
msg=driver.find_element(By.XPATH,"//div[@class='_9ay7']").text
print(msg)
msg1=driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print(msg1)