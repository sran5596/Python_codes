from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,"//*[@id='dob']").click()
month=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_value('11')
year=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_value('1996')
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in alldates:
    if ele.text=='17':
        ele.click()
        break

driver.find_element(By.XPATH,"//*[@id='dob']").get_attribute('value')
time.sleep(5)