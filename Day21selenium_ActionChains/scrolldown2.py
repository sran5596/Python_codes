from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#move use the pixel
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("print the value pixels:",value)

#move the field based on the item
zim=driver.find_element(By.XPATH,"//td[normalize-space()='Zimbabwe']")
driver.execute_script("arguments[0].scrollIntoView();",zim)
v1=driver.execute_script("return window.pageYOffset;")
print("pixels:",v1)

#mov to the bottm of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
v2=driver.execute_script("return window.pageYOffset;")
print("pixels:",v2)

#move the top the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
v3=driver.execute_script("return window.pageYOffset;")
print("pixels:",v3)

