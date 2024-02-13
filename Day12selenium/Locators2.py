#CLASS_NAME -- used to find the sliders/images in page
#TAG_NAME -- used to find total links in the page
#here used the [[find_elements]]
#website--driver.get("https://www.facebook.com/login/")

#TAG_NAME USED AND BELOW CODE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
#driver.find_elements(By.CLASS_NAME,"")
link=driver.find_elements(By.TAG_NAME,"a")
print(type(link))
print(len(link))
driver.close()

#class_name ex
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://automationpractise.com/index.php")
slides=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(type(slides))
print(len(slides))

driver.close()

