from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\\drivers\\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
def edge():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\msedgedriver.exe")
    driver=webdriver.Edge(service=obj)
    return driver

#driver=edge()
driver=chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
exp_title=driver.title
act_title="Dashboard / nopCommerce administration"
if exp_title==act_title:
    print("test passed")
else:
    print("test faitled")
driver.quit()
