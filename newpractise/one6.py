from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("s.raveendra7416@gmail.com")

driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("sraveendra009403@@")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='_9lsa']//div[1]").click()
driver.find_element(By.XPATH,"//div[@class='_9lsa']//div[1]").click()
# driver.find_element(By.XPATH,"//*[@id='u_0_4_JI']").click()
#driver.find_element(By.CSS_SELECTOR,"div#u_0_4_JI").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='loginbutton']").click()