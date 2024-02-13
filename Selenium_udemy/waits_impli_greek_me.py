from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
def impli_wait():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
driver=impli_wait()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("carrot")
driver.find_element(By.XPATH,"//a[@class='increment']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='decrement']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//button[normalize-space()='ADD TO CART']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahul")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/button").click()
err_alert=driver.find_element(By.XPATH,"//span[@class='promoInfo']").text
if err_alert=="Invalid code ..!":
    print("its error rahulpromo code not their")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/button").click()
time.sleep(5)
sus_alert=driver.find_element(By.XPATH,"//div[@class='promoWrapper']/span").text
time.sleep(5)
if sus_alert=="Code applied ..!":
    print("rahulsheetyacademy code is their and applied")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='chkAgree']").click()
time.sleep(5)
dropdown=Select(driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/select"))
dropdown.select_by_visible_text("India")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']")
time.sleep(5)
# alert=driver.find_element(By.XPATH,"//span[contains(text(),'Thank you, your order has been placed successfully')]").text
# print(alert)
print(driver.current_url)
title=driver.title
print(title)
assert title=="GreenKart - veg and fruits kart"
driver.quit()