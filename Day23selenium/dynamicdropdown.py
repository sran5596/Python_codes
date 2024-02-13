from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os #get current working directory
def dropdown():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver= webdriver.Chrome(service=obj)
    return driver
driver=dropdown()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
one=driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']")
driver.execute_script("arguments[0].scrollIntoView();",one)
pixels=driver.execute_script("return window.pageYOffset;")
print("pixels:",pixels)
countrylist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
for cou in countrylist:
    if cou.text=="India":
        cou.click()
        break
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").get_attribute("value")
time.sleep(5)
#below statements take screenshot
driver.save_screenshot("D:\\drivers\\dummy.png") #its store you given location
driver.save_screenshot(os.getcwd()+"dummy.png") # its store the current location directory
time.sleep(5)