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
#moved the based on pixels
driver.execute_script("window.scrollBy(0,3000)","") #syntax for scroll down based on pixels

value=driver.execute_script("return window.pageYOffset;") # its for printing purpose

print("value of pixel value moved : ",value)
time.sleep(5)
#moven the basewd on item
flag=driver.find_element(By.XPATH,"//td[normalize-space()='Luxembourg']")

driver.execute_script("arguments[0].scrollIntoView();",flag) # its identify the element syntax go to that place
value1=driver.execute_script("return window.pageYOffset;")
print("value of the pixels value1 :",value1)
time.sleep(5)
#moved to end of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")# its go top of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")# its go bottom of the page

value2=driver.execute_script("return window.pageYOffset")
print("value of the pixel moved value2:",value2)
time.sleep(5)
#moved to top of the pageument.body.scrollHeight)") # it go first of the page

value3=driver.execute_script("return window.pageYOffset")
print("value of the pixel moved value2:",value3)
time.sleep(5)
