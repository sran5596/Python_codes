
import openpyxl
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ChromeOptions
alert=webdriver.ChromeOptions()
alert.add_argument("--disable-notifications")
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
#its for the scrolling the down direction

one=driver.find_element(By.XPATH,"//input[@id='principal']") #webelement created
driver.execute_script("arguments[0].scrollIntoView();",one) #its for the scrolling down
# one2=driver.execute_script("retrun window.pageYOffset;") # its for printing the down words
# print("pixels of the one:",one2) #its print the pixels
file="D:\\Datasets\\ddttest.xlsx" # file path
from Day24selenium_excel_actions import Utility #imported the code from Day24selenium
rows=Utility.getRowCount(file,"Sheet1") #used the row count method
try:
    for r in range(2,rows+1): #for loop to repaet the
        pric=Utility.readData(file,"Sheet1",r,1)
        rateofinterest=Utility.readData(file,"Sheet1",r,2)
        pre1=Utility.readData(file, "Sheet1", r,3)
        pre2=Utility.readData(file, "Sheet1", r,4)
        fre=Utility.readData(file, "Sheet1", r,5)
        exp_value=Utility.readData(file, "Sheet1", r,6) # its string
#identify the elemenst
        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(pre1)
        value=Select(driver.find_element(By.XPATH,"//*[@id='tenurePeriod']")) # Select used drop down
        value.select_by_visible_text(pre2)
        value2=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
        value2.select_by_visible_text(fre)
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='CTR PT15']/a[1]/img").click()
        actual_value=driver.find_element(By.XPATH,"//span[@class='gL_27']/strong").text # its also string
        if float(exp_value)==float(actual_value):
            print("test Passed")
            Utility.writeData(file,"Sheet1",r,8,"passed")
            Utility.fillGreenColour(file,"Sheet1",r,8)
        else:
            print("test ailed")
            Utility.writeData(file,"sheet1",r,8,"Failed")
            Utility.fillRedColour(file,"sheet1",r,8)
        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(5)
except Exception as e:
    print(e)
driver.close()