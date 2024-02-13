from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
fr=driver.find_element(By.XPATH,"//*[@id='iframeResult']")
driver.switch_to.frame(fr)
one=driver.find_element(By.XPATH,"//*[@id='field1']")
one.clear()
one.send_keys("RAVEENDRA GREAT")
button=driver.find_element(By.XPATH,"/html/body/button")
act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(5)