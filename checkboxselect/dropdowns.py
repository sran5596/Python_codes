from datetime import time
import time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
lists=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
# lists.select_by_value("option1")
time.sleep(5)
print(len(lists.options))
one=lists.options
for i in lists.options:
    print(i.text)
time.sleep(2)
check=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
print(check.is_selected())
for i in one:
    if i.text=="option2":
        i.click()
        break
time.sleep(5)


