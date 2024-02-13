#close()- it close the sing window browser (driver is foucsed) it not stop the other windows process
#quit() -- it close the all browser windows and process also, and it stop all process

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
#driver.get("https://www.flipkart.com/")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.close()
driver.quit()
time.sleep(5)

