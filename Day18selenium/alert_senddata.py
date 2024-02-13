from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
one=driver._switch_to.alert
one.send_keys("Raveendra") # its send the data to the slert
one.accept() # its accept the alert
#one.dismiss() # its dis miss the alert
#print(one.text)
time.sleep(5)