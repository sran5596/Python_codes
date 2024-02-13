from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def checkbox():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\\drivers\\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
driver=checkbox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("S.Raveendra")
# driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# alert=driver.switch_to.alert
# print(alert.text)
# time.sleep(5)
# alert.accept()
# time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
alert1=driver.switch_to.alert
time.sleep(5)
alert1.accept()

driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
time.sleep(5)
alert1.dismiss()
#print(alert1.text)

