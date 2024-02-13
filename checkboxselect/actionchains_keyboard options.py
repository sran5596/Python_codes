from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
import time
import os
obj=Service("D/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
act=ActionChains(driver)
driver.get("https://text-compare.com/")
driver.maximize_window()
ele=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.send_keys("Hello")
#Ctrl+a
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
#Ctrl+c
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
#ctrl+tab
# act.key_down(Keys.CONTROL)
# act.send_keys("tab")
# act.key_up(Keys.CONTROL)
# act.perform()
act.send_keys(Keys.TAB).perform()
#ctrl+v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
ele1=driver.find_element(By.XPATH,"//div[@class='compareButtonText']")
driver.execute_script("arguments[0].scrollIntoView();",ele1)
ele1.click()
ele2=driver.find_element(By.XPATH,"/html/body/div[2]/span[3]")
driver.execute_script("arguments[0].scrollIntoView();",ele2)
print(ele2.text)
time.sleep(2)
driver.quit()


