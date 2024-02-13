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
#direct select
# option2checkbox=driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']")
# option2checkbox.click()
# print(option2checkbox.text)
# option2checkbox.get_attribute("value")
#second way
options=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(options))
for choice in options:
    if choice.get_attribute("value")=="option2":
        choice.click()
        choice.is_selected()
        break
time.sleep(5)
driver.quit()

