from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://mypage.rediff.com/login/dologin")
driver.find_element(By.XPATH,"//input[@value='Login']").click()
one=driver.switch_to.alert
one.accept()
time.sleep(4)