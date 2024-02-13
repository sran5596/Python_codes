import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("http://www.deadlinkcity.com/")
tg=driver.find_elements(By.TAG_NAME,"a")
count=0
for one in tg:
    url=one.get_attribute("href")
    try:
        reg=requests.head(url)
    except Exception as e:
        print(e)
    if reg.status_code>=400:
        print(url,"Broken links")
        count+=1
    else:
        print("valid links")
print("total count",count)

