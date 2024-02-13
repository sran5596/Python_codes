import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
obj=Service("D:\drivers\chromedriver.exe")
# obj=Service("D:\drivers\msedgedriver.exe")
driver=webdriver.Chrome(service=obj)
# driver=webdriver.Edge(service=obj)
# driver.get("https://admin-demo.nopcommerce.com/login")
driver.get("https://www.amazon.in/")
#css-tagname#value of id
# driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
#css-tagname.value ofclass
#driver.find_element(By.CSS_SELECTOR,"a.nav-a").click()
#css-tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input[dir='auto']").send_keys("pen")
#css-tagname.value of class[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input.nav-input[id='nav-search-submit-button']").click()
time.sleep(5)
print(driver.current_url)
