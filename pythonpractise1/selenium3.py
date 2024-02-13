from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import openpyxl
import time
from selenium.webdriver.chrome.service import Service
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.facebook.com/signup/")
from Day24selenium_excel_actions import Utility
file="D:\\Datasets\\fbdata.xlsx"
rows=Utility.getRowCount(file,"Sheet1")
try:
    for r in rows(2,rows+1):
        firstname=Utility.readData(file,"Sheet1",r,1)
        Surname=Utility.readData(file,"Sheet1",r,2)
        Email=Utility.readData(file,"Sheet1",r,3)
        Password=Utility.readData(file,"Sheet1",r,4)
        Day=Utility.readData(file,"Sheet1",r,5)
        Month=Utility.readData(file,"Sheet1",r,6)
        Year=Utility.readData(file,"Sheet1",r,7)
        Gender=Utility.readData(file,"Sheet1",r,8)
        driver.find_element(By.XPATH,"//input[@id='u_0_b_Dq']").send_keys(firstname)
        driver.find_element(By.XPATH,"//input[@id='u_0_d_FS']").send_keys(Surname)
        driver.find_element(By.XPATH,"//input[@id='u_0_g_pS']").send_keys(Email)
        driver.find_element(By.XPATH,"//input[@id='password_step_input']").send_keys(Password)
        dayselect=Select(driver.find_element(By.XPATH,"//*[@id='day']"))
        dayselect.select_by_value(Day)
        monthselect=Select(driver.find_element(By.XPATH,"//*[@id='month']"))
        monthselect.select_by_value(Month)
        yearselect=Select(driver.find_element(By.XPATH,"//select[@id='year']"))
        yearselect.deselect_by_value(Year)
        driver.find_element(By.XPATH,"//label[@for='u_0_5_XC']").send_keys(Gender)
        time.sleep(5)
except Exception as e:
    print(e)
driver.quit()
