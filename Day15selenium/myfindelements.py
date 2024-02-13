import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH,"//*[@id='ctl00_mainContent_ddl_originStation1_CTXTaction']").click()
# t=driver.find_elements(By.TAG_NAME,"a")
# print(len(t))
# t1=Select(driver.find_element(By.XPATH,"//select[@id='ctl00_mainContent_ddl_originStation1']"))
# time.sleep(5)
# t1.select_by_value("IXG")
list2=driver.find_elements(By.TAG_NAME,"option")
print(len(list2))

list1=driver.find_elements(By.TAG_NAME,"a")
print(len(list1))
for y in list1:
    #print(y.text)
    if y.text=="Goa (GOI)":
        y.click()
#print(driver.find_element(By.XPATH,"//*[@id='ctl00_mainContent_ddl_originStation1_CTXTaction']").get_attribute("value"))
# r=driver.find_element(By.XPATH,"//*[@id='ctl00_mainContent_ddl_originStation1_CTXTaction']").get_attribute("value")
# print(r)
time.sleep(5)
driver.maximize_window()
print(driver.title)
driver.close()