from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/driveers/msedgedriver.exe")
ops=webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Edge(service=obj,options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
