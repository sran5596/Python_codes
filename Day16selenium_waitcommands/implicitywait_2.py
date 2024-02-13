import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
google=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
google.send_keys("Selenium")
google.submit()
#time.sleep(5)
driver.find_element(By.XPATH,"//h3[normalize-space()='7 Science-Based Health Benefits of Selenium']").click()
# driver.find_element(By.XPATH,"//h3[normalize-space()='7 Science-Based Health Benefits of Selenium']").get_attribute("value")
