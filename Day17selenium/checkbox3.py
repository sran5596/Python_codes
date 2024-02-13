from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#che=driver.find_elements(By.CLASS_NAME,"form-check-label") #i am written
check=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(check))
# for li in che: #its select the all items
#     li.click()
for list in check:
    #print(list.get_attribute('id')) #sir given morethan one eleemnt text not work so use get_attribute
    weekname=list.get_attribute('id')
    if weekname=='monday' or weekname=='Sunday':
        list.click()
time.sleep(5)




