from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,"//input[@id='dob']").click()
mth=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
mth.select_by_value("5")
yr=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
yr.select_by_value("1998")
days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for one in days:
    if one.text=='14':
        one.click()
        break
time.sleep(5)