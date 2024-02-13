from Day24selenium_excel_actions import Utility
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1")
one=driver.find_element(By.XPATH,"//span[@class='male']")
mywiat=WebDriverWait(driver,10)
mywiat.until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='male']")))
one.click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Raveendra")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Sampathi")
day=Select(driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]"))
day.select_by_value("17")
month=Select(driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]"))
month.select_by_value("12")
year=Select(driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]"))
year.select_by_value("1998")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("raveendra@123")
time.sleep(5)
one=driver.find_element(By.XPATH,"//a[normalize-space()='Shopping cart']")
driver.execute_script("arguments[0].scrollIntoView();",one)
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)