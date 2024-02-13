from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
def one():
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
driver=one()
# driver.get("https://demo.nopcommerce.com/")
# #it foucs on the old tab
# print(driver.title)
# READ=Keys.CONTROL+Keys.ENTER # it create the new tab
# driver.find_element(By.XPATH,"//a[normalize-space()='About us']").send_keys(READ)
# print(driver.title)
# time.sleep(5)
# # driver.close()
# #it opn the new tab
# driver.get("https://www.foundit.in/")
# driver.switch_to.new_window("tab") # it create the new tab
# print(driver.title)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")# in new thab it open
# print(driver.title)
#cretae another for open the new window
driver.get("https://www.flipkart.com/")
driver.switch_to.new_window("window") # it create the new browser
driver.get("https://money.rediff.com/gainers/bse/dailygroupa")

#