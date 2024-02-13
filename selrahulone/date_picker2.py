from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
# date=driver.find_element(By.XPATH,"//*[@id='datepicker']")
# date.send_keys("12/17/1996")
# print(date.get_attribute('value'))
# time.sleep(5)
month="December"
year="1997"
day='17'
date = driver.find_element(By.XPATH, "//*[@id='datepicker']")
date.click()
while True:
    lmonth=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    lyear=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    # day=driver.find_element(By.XPATH,"")
    if lyear==year and lmonth==month:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==day:
        ele.click()
        break
time.sleep(5)
print(driver.find_element(By.XPATH,"//*[@id='datepicker']").get_attribute('value'))

