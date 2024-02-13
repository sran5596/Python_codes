from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#che=driver.find_elements(By.CLASS_NAME,"form-check-label") #i am written
che=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(che))
for li in che:
    print(li.get_attribute('id'))
    li.click()
    # if li.text=="Wednesday":
    #     li.click()
    #     break
time.sleep(5)
#driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[4]/label").click()
#time.sleep(5)
