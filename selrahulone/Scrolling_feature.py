from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(5)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.PageYOffset;")
print("number of pixels moved :",value)