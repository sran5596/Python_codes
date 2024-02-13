import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.get("https://demo.nopcommerce.com/books")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(0.3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(6)
elements=driver.find_elements(By.TAG_NAME,"a")
print(len(elements))
print(elements[0].text)
for i in elements:
    print(i.text)
    if i.text=="Sitemap":
        i.click()
        break
time.sleep(5)
driver.quit()