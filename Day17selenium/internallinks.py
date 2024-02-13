from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
#single element click
time.sleep(5)
# #driver.find_element(By.LINK_TEXT,"Digital downloads").click() # link_text used
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click() # partial_link_text used
#find many links in the page
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for one in links:
    print(one.text)
    if one.text=="Books":
        one.click()
        break
        time.sleep(5)


