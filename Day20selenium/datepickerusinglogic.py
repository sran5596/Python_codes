#Non-standered
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
fr=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
driver.switch_to.frame(fr)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
month,year,date="June","2022","14" # [[assigned the values u need first ass -string-
while True: # writtedn the logic while why because we dont the correct date through to date picker
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text #comman xpath for year
    mth=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text # comman Xpath for month
    if month==mth and year==yr: #logic
        break  # must give the -break- while is excueted agaain and again untill fail so used the brak
    else: #if month and year not matched click right arrow button
        #driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a") # thid is date comman xpath used [elements]
for one in days:  # for loop used to iterate
    if one.text==date:  # if used to match the date we needed
        one.click() # click once you reach the date
        break
time.sleep(5)