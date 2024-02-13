from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
mywait=WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
cale=mywait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/form/div[4]/div[2]/div/div[5]/div[2]/div[2]/div[2]/div[3]/div/div[4]/button")))
# driver.find_element(By.XPATH,"//*[@id=flightSearchContainer']/div[4]/button").click()
cale.click()
days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td")
for i in days:
    if i.get_attribute('a')=="15":
        i.click()
total=driver.find_element(By.XPATH,"//*[@id='ctl00_mainContent_view_date1']").get_attribute('name')
print(total)
time.sleep(6)