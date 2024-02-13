from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
act=ActionChains(driver)
act.context_click(button).perform()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/ul/li[7]").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(5)