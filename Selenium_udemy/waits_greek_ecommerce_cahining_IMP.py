from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
def impli_wait():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
driver=impli_wait()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("br")
#till now used the common xpath and used the find elements
products=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(products))
count=len(products)
assert count>0
time.sleep(5)
#chaining used here
for list in products:
    # list.find_element(By.XPATH,"//div[@class='products']/div/div/a[2]").click()
    list.find_element(By.XPATH,"div/button").click()
time.sleep(5)