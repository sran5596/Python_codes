#driver.switch_to.window()-its for chamnge windows

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
obj=Service("D:\drivers/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
# mywiat=WebDriverWait(driver,10,poll_frequency=2)
mywait=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#siongle window handle this
# idone=driver.current_window_handle
# print(idone)

#multiple window handlebtn btn-orange btn-outline btn-xl page-scroll download-button
# mywait=WebDriverWait(driver,20)
two=mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")))
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
two.click()
time.sleep(10)
# three=mywait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/footer[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")))
# time.sleep(10)
# three.click()
# four=mywait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/footer[1]/section[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")))
# time.sleep(22)
# four.click()
ids=driver.window_handles
# print(ids[0])
# time.sleep(5)
# print(ids[1])
# parent=ids[0]
# fchild=ids[1]
# schild=ids[2]
# tchild=ids[3]

#printing the titles all at atime
# driver.switch_to.window(parent)
# print(driver.title)
# driver.switch_to.window(fchild)
# print(driver.title)
for i in ids:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title=="OrangeHRM HR Software | OrangeHRM" or driver.title=="OrangeHRM":
        driver.close()
time.sleep(2)