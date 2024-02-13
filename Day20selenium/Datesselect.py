#1)standard elements
#2)Non-standrad elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.facebook.com/reg/")
day=Select(driver.find_element(By.XPATH,"//*[@id='day']"))
day.select_by_value("14")
month=Select(driver.find_element(By.XPATH,"//*[@id='month']"))
month.select_by_value("6")
year=Select(driver.find_element(By.XPATH,"//*[@id='year']"))
year.select_by_value("1998")
time.sleep(5)

driver.get("https://jqueryui.com/datepicker/")
fr=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
driver.switch_to.frame(fr)
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("14/06/1998")
time.sleep(5)
driver.back()
time.sleep(5)

