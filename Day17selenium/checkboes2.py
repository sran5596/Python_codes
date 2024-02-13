from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#che=driver.find_elements(By.CLASS_NAME,"form-check-label") #i am written
che=driver.find_elements(By.XPATH,"//input[@type='radio' and @name='optionsRadios']")
print(len(che))
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(5)





















