from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
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
# wait=WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='product-action']/button")))
time.sleep(5)
for list in products:
     list.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter promo code']")))
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
alert=driver.find_element(By.XPATH,"//span[@class='promoInfo']").text
print(alert)