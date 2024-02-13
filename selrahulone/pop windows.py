from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
# mywiat=WebDriverWait(driver,10,poll_frequency=2)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# seb=mywiat.until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div/ul/li[1]/button")))
# seb.click()
# time.sleep(2)
# alert=driver.switch_to.alert
# time.sleep(2)
# alert.accept()
# time.sleep(2)

# alttext=driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button")
# print(alttext.text)
# time.sleep(2)
#
# sctext=driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button")
# sctext.click()
# # print(sctext.text)
# one=driver.switch_to.alert
# one.accept()
# time.sleep(2)
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
# alt=driver.switch_to.alert
# time.sleep(2)
# alt.send_keys("welcome")
# time.sleep(2)
# # print(alt.text)
# # alt.accept()
# # time.sleep(2)
# time.sleep(5)

#Authentication popups
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# textone=driver.find_element(By.XPATH,"//*[@id='content']/div/p").text
# assert "credentials"  in textone


