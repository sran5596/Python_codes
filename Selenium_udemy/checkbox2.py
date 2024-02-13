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
radio=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
for select in radio:
    if select.get_attribute("value")=="radio2":
        select.click()
        assert select.is_selected()
        break
time.sleep(5)
driver.quit()