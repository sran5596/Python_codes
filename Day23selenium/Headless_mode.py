from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
#its for chrome
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=obj,options=ops)
    return driver
def headless_edge(): #its for edge headlessmode
    from selenium.webdriver.edge.service import Service
    obj = Service("D:\drivers\msedgedriver.exe")
    ops = webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Edge(service=obj, options=ops)
    return driver
#firefox also same code import firefox service and webdriver.firefoxoptions 
driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
