from datetime import time
import time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
#LINKS BASED ON THE TEXT
# driver.get("https://www.amazon.in/ref=nav_logo")
# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
# for i in links:
#     print(i.text)
#     if i.text=="Amazon Science":
#         i.click()
#         break
# time.sleep(5)
#broken links
# driver.get("http://www.deadlinkcity.com/")
# links=driver.find_elements(By.TAG_NAME,"a")
# count=0
# for link in links:
#     url=link.get_attribute('href')
#     try:
#         res=requests.head(url)
#     except:
#         None
#     if res.status_code>=400:
#         print(url,"url is broken")
#         count+=1
#     else:
#         print(url,"url is working fine")
# print("Total number of broken links:",count)



