from selenium import webdriver
import time
from Day24selenium_excel_actions import Utility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1")
file="D:\Datasets\excelutilityexample.xlsx"
rows=Utility.getRowCount(file,"Sheet1")
try:
    for r in range(2,rows+1):
        gender=Utility.readData(file,"Sheet1",r,1)
        fname=Utility.readData(file,"Sheet1",r,2)
        lname=Utility.readData(file,"Sheet1",r,3)
        sday=Utility.readData(file,"Sheet1",r,4)
        month=Utility.readData(file,"Sheet1",r,5)
        year=Utility.readData(file,"Sheet1",r,6)
        email=Utility.readData(file,"Sheet1",r,7)
        company_name=Utility.readData(file,"Sheet1",r,8)
        password=Utility.readData(file,"Sheet1",r,9)
        con_pass=Utility.readData(file,"Sheet1",r,10)
        Utility.fillGreenColour(file,"Sheet1",r,11)


        mf=driver.find_elements(By.XPATH,"//div[@id='gender']//label")
        if mf==gender:
            print(mf.text)
            mf[0].click()
#         driver.find_element(By.XPATH,"//input[@id='gender-male']").send_keys(gender)

        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys(fname)
        driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys(lname)
        dys=driver.find_elements(By.XPATH,"//select[@name='DateOfBirthDay' and @aria-invalid='false']//option")
        if dys==sday:
            dys.click()
        time.sleep(10)
# dy=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
# time.sleep(5)
# dy.select_by_value(sday)
        mth=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))
        mth.select_by_visible_text(month)
        time.sleep(5)
# yrs=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']"))
# yrs.select_by_value(year)
        yrs=driver.find_elements(By.XPATH,"//select[@name='DateOfBirthYear']//option")
        if yrs==year:
            yrs.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@id='Company']").send_keys(company_name)
        driver.find_element(By.XPATH,"//input[@id='Password']").send_keys(password)
        driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys(con_pass)

except Exception as e:
    print(e)
time.sleep(15)
driver.quit()


