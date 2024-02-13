from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
ele=driver.execute_script("return window.pageYOffset;")
print("last:",ele)
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
ele1=driver.execute_script("return window.pageYOffset;")
print("first:",ele1)

#element based
item=driver.find_element(By.XPATH,"//a[normalize-space()='Broken Link']")
driver.execute_script("arguments[0].scrollIntoView();",item)
gg=driver.execute_script("return window.pageYOffset;")
print(gg)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1600)","")
hoo=driver.execute_script("return window.pageYOffset;")
print(hoo)
time.sleep(5)
