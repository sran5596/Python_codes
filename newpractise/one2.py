from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print(driver.title)
act=driver.title
exp="Dashboard / nopCommerce administration"
if act==exp:
    print("great")
else:
    print("not")
print(driver.current_url)