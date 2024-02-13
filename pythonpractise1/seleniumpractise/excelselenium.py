import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Day24selenium_excel_actions import Utility
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
file="D:\\Datasets\\ddttest.xlsx"
rows=Utility.getRowCount(file,'Sheet1')
try:
    for r in rows(2,rows+1):
        pri=Utility.readData(file,"Sheet1",r,1)
        rate=Utility.readData(file,"Sheet1",r,2)
        pre1=Utility.readData(file,"Sheet1",r,3)
        pre2=Utility.readData(file, "Sheet1", r, 4)
        fre=Utility.readData(file, "Sheet1", r, 5)
        exp_value=Utility.readData(file, "Sheet1", r, 6)
    # Utility.readData(file, "Sheet1", r, 7)
    # Utility.readData(file, "Sheet1", r, )
        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pri)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rate)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(pre1)
        time.sleep(5)
        duration=Select(driver.find_element(By.XPATH, "//*[@id='tenurePeriod']"))
        duration.select_by_visible_text(pre2)
        type=Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
        type.select_by_visible_text(fre)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
        act_value=driver.find_element(By.XPATH,"//span[@class='gL_27']/strong").text
        if float(exp_value)==float(act_value):
            Utility.writeData(file,"Sheet1",r,8,"Passed")
            Utility.fillGreenColour(file,"Sheet1",r,8)
            print("test passed")
        else:
            Utility.writeData(file,"Sheet1",r,8,"Failed")
            Utility.fillRedColour(file,"sheet1",r,8)
            print("test failed")
        driver.find_element(By.XPATH,"//img[@class='PL5']").click()
        driver.quit()
except Exception as e:
    print(e)





