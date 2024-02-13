from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//label[@for='bmw']").click()
time.sleep(5)