from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
import time
import os
obj=Service("D/drivers/msedgedriver.exe")

ops=webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--ingnore-certificate-errors")
ops.add_argument('--ingnore-ssl-errors')
driver=webdriver.Edge(service=obj,options=ops)
mywait=WebDriverWait(driver,10)

act=ActionChains(driver)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
ele=driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]")
driver.save_screenshot("D:\pythonprograms\checkboxselect\do.png")
mywait.until(EC.presence_of_element_located((By.XPATH,"//tbody/tr[1]/td[5]/a[1]"))).click()
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# ele.click()
time.sleep(5)
