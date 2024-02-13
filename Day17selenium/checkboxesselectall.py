from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
lit=driver.find_elements(By.XPATH,"//div[@class='card-body']//div[2]//div//label")
print(len(lit))
for one in lit:
    if one.text=="Mabl":
        one.click()
        break
time.sleep(5)