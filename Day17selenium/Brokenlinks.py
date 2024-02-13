import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
time.sleep(5)
links=driver.find_elements(By.TAG_NAME,"a")
for one in links:
    print(one.text)
count=0
for one in links:
    url=one.get_attribute("href")
    try:
        reg=requests.head(url)
    except:
        None
    if reg.status_code>=400:
        print(url,"broken links")
        count+=1
    else:
        print("valid links")
print("total number of brokenlinks:",count)
