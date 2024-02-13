# title
# current_url
# page_source

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
