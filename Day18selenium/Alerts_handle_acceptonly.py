#alert not webelement

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
time.sleep(5)
button=driver.switch_to.alert
button.accept() #it accept the alert
#button.dismiss() #its dismiss the alert
time.sleep(5)