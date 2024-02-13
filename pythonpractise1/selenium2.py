from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import openpyxl
import time
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
driver=chrome()
driver.get("https://www.facebook.com/signup/")
from Day24selenium_excel_actions import Utility
file="D:\\Datasets\\fbdata.xlsx"
rows=Utility.getRowCount(file,"Sheet1")
try:
    for r in range(2,rows+1):
        firstname=Utility.readData(file,"Sheet1",r,1)
        Surname=Utility.readData(file,"Sheet1",r,2)
        Email=Utility.readData(file,"Sheet1",r,3)
        reenter=Utility.readData(file,"Sheet1",r,4)
        Password=Utility.readData(file,"Sheet1",r,5)
        Day=Utility.readData(file,"Sheet1",r,6)
        Month=Utility.readData(file,"Sheet1",r,7)
        Year=Utility.readData(file,"Sheet1",r,8)
        Gender=Utility.readData(file,"Sheet1",r,9)
        time.sleep(5)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(firstname)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Surname)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Email)
        time.sleep(5)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]").send_keys(reenter)
        time.sleep(4)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/input[1]").send_keys(Password)
        time.sleep(5)
        # days=driver.find_elements(By.XPATH,"//select[@id='day']/option")
        # if days==Day:
        #     days.click()
        time.sleep(5)
        dayselect=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/div[2]/span[1]/span[1]/select[1]"))
        dayselect.select_by_value(Day)
        time.sleep(3)
        monthselect=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/div[2]/span[1]/span[1]/select[2]"))
        monthselect.select_by_value(Month)
        yearselect=Select(driver.find_element(By.XPATH,"//select[@id='year']"))
        yearselect.select_by_value(Year)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[7]/span[1]/span[2]/label[1]").send_keys(Gender)
        time.sleep(5)
except Exception as e:
    print(e)
driver.quit()


