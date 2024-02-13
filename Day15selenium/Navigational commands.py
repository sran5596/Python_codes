#back()-it goes back window
#forward()-it goes forward window
#refresh()-it refresh the page

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
print(driver.title)
time.sleep(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
time.sleep(5)
driver.refresh()
driver.back()
driver.forward()
#print(driver.title)
time.sleep((5))
driver.quit()