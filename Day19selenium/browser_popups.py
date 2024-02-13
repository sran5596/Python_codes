from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj,options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()