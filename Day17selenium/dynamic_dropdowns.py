import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
time.sleep(5)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(5)
#driver.find_element(By.XPATH,"//a[@id='ui-id-169']").click()
time.sleep(5)
cop=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a ")
print(len(cop))
for one in cop:
    if one.text=="India":
        one.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))






# for i in list:
#     one=i.get_attribute("id")
#     if one=="India":
#         i.click()
# time.sleep(5)