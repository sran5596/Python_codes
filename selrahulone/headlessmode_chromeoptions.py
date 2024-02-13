from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def headless_chrome():
    ops=webdriver.ChromeOptions()
    obj=Service("D:\drivers\chromedriver.exe")
    ops.headless=True
    ops.add_argument("--headless")
    ops.add_argument("--disable-notifications")
    driver=webdriver.Chrome(service=obj,options=ops)
    return driver

def headless_firefox():
    ops=webdriver.FirefoxOptions()
    obj=Service("D:\drivers\geckodriver.exe")
    ops.headless=True
    driver=webdriver.Firefox(service=obj,options=ops)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
assert driver.title=="nopCommerce demo store"

