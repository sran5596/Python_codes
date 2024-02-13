from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//*[@id='radio-btn-example']/fieldset/label[1]/input").click()
drop_down=Select(driver.find_element(By.XPATH,"//*[@id='dropdown-class-example']"))
time.sleep(5)
drop_down.select_by_index(3)
time.sleep(5)
drop_down.select_by_visible_text("Option2")
time.sleep(5)
# drop1=Select(driver.find_element(By.XPATH,"//*[@id='mousehover']"))
# h=drop1.select_by_visible_text("Top").text
# print(h)
