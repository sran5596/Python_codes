import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//*[@id='pass']").send_keys('anc')
time.sleep(3)
#driver.find_element(By.XPATH,"//*[@class='_9lsb _9ls8' and @id='u_0_4_Jj']").click()
# driver.find_element(By.XPATH,"//*[@class='_9lsb _9ls8' or @class='_9lsb _9ls9']").click()
# time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(@class,'_9lsb')]").click()
time.sleep(5)