from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("ind")
list=driver.find_elements(By.CLASS_NAME,"ui-corner-all")
print(len(list))
for cou in list:
    print(cou.text)
    if cou.text=="india":
        cou.click()
        break
print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value")=="india"

