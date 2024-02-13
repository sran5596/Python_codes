import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH,"//*[@id='autosuggest']").send_keys("abc")
time.sleep(4)
li1=driver.find_elements(By.CLASS_NAME,"ui-corner-all")#class name used to find how many here
print(len(li1))
for i in li1:
    if i.text=="India":
        i.click()
        break

