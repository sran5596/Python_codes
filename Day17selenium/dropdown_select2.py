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
driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(6)
lis=Select(driver.find_element(By.XPATH,"//*[@id='input-country']"))
lis.select_by_visible_text("American Samoa")
for one in lis:
    print(one.text)
time.sleep(5)