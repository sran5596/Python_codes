from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.XPATH,"//input[@id='Email']").clear()
# driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@id='Password']").clear()
# driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
links=driver.find_elements(By.LINK_TEXT,"//a")
print(len(links))