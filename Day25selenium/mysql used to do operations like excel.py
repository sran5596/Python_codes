from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import mysql.connector
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
try:
    con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
    cur=con.cursor()
    cur.execute("select  * from ca")
    for row in cur:
        principle=row[0]
        Rate_of_interest=row[1]
        period1=row[2]
        period2=row[3]
        Frequency=row[4]
        Maturity_value=row[5]
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(Rate_of_interest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)
    value=Select(driver.find_element(By.XPATH,"//*[@id='tenurePeriod']")) # Select used drop down
    value.select_by_visible_text(period2)
    value2=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    value2.select_by_visible_text(Frequency)
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='CTR PT15']/a[1]/img").click()
    actual_value=driver.find_element(By.XPATH,"//span[@class='gL_27']/strong").text # its also string
    if float(actual_value)==float(Maturity_value):
        print("Test passed")
    else:
        print("test failed")
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()

except Exception as e:
    print(e)
driver.quit()