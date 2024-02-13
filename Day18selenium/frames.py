from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame") #here we chance to give the id or name or webelement
driver.find_element(By.LINK_TEXT,"org.openqa.selenium.bidi.log").click()
time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"BaseLogEntry").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//div[@class='topNav']//a[normalize-space()='Help']").click()
driver.switch_to.parent_frame()
time.sleep(5)

