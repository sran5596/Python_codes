from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.facebook.com/signup/")
# driver.find_element("//select[@id='day']").click()
# day=Select(driver.find_element(By.XPATH,"//select[@id='day']"))
# day.select_by_value(14)
# time.sleep(5)
days=driver.find_elements(By.XPATH,"/select[@id='day']")
for r in days:
    if r.text==14:
        r.click()
time.sleep(5)