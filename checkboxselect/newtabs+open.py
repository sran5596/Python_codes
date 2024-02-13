from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
import os
location=os.getcwd()
import time
obj=Service("D:/drivers/msedgedriver.exe")
ops=webdriver.EdgeOptions()
# ops.headless=True # its not worked

ops.add_argument("--headless") # its worked
driver=webdriver.Edge(service=obj,options=ops)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
driver.save_screenshot(location+"\\demo1.png")
time.sleep(2)
ect=ActionChains(driver)
new=Keys.CONTROL+Keys.ENTER
driver.find_element(By.XPATH,"//a[normalize-space()='Sitemap']").send_keys(new)
driver.save_screenshot(location+"\\demo2.png")



