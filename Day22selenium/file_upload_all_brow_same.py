from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
driver=chrome()
driver.get("https://www.foundit.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()

driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("D:\Resumes\Shaik Dhudhuvalli Resume.docx")
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='action-cta']").click()
time.sleep(5)