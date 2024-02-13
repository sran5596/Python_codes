from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(10)
driver.maximize_window()
mywiat=WebDriverWait(driver,10)

# move the pixels
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of 3000 pixels:",value)
#moved the element
element=driver.find_element(By.XPATH,"//td[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();",element)
element1=driver.execute_script("return window.pageYOffset;")
print("Number of india pixels:",element1)
time.sleep(5)

#go to the footer
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
ele=driver.execute_script("return window.pageYOffset;")
print("Number of last pixels:",ele)

#go to the header
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
ele2=driver.execute_script("return window.pageYOffset;")
print("number of first pixels:",ele2)


