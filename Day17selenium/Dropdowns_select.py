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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
lis=Select(driver.find_element(By.XPATH,"//*[@id='dropdown-class-example']"))

#using the built_in funstions below selected mean
# lis.select_by_value("option2") #select_by_value its built in function
# time.sleep(5)
# lis.select_by_visible_text("Option3") # this also
# time.sleep(5)
# lis.options # it capture the all ontions [[options]]]
# print(len(lis.options))
# for i in lis.options:
#     print(i.text)

lis.options # its capture the total elemenst
for i in lis.options:
    print(i.text)
    if i.text=="Option3":
        i.click()
        break
time.sleep(5)

