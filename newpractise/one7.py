from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
# list=driver.find_elements(By.XPATH,"//ul[@class='top-menu mobile']//li[1]")
# print(len(list))
# time.sleep(5)
driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//li[@class='inactive']//a[normalize-space()='Desktops']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Desktops").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='item-grid']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
# buttons=Select(driver.find_element(By.XPATH,"//select[@id='product_attribute_2']"))
# buttons.select_by_value("3")
# buttons=Select(driver.find_element(By.XPATH,"//div[@class='attributes']//dl//dd[2]//select"))
#buttons.select_by_value("3")
driver.find_element(By.XPATH,"//select[@id='product_attribute_2']")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='product_attribute_2']/option[3]").click()
time.sleep(5)
check=driver.find_element(By.XPATH,"//input[@id='product_attribute_3_6']")
check.is_displayed()
driver.find_element(By.XPATH,"//input[@id='product_attribute_3_6']".click())
driver.find_element(By.XPATH,"//button[@id='add-to-cart-button-1']").click()
driver.find_element(By.XPATH,"//span[@class='cart-label']").click()
driver.find_element(By.XPATH,"//button[@class='remove-btn']").click()
time.sleep(5)




driver.find_element(By.XPATH,"//button[@id='add-to-cart-button-1']").click()
