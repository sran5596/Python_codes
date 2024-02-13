from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH,"//input[@id='search']").send_keys("SDET postman")
# driver.find_element(By.ID,"search").send_keys("SDET").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']//div").click()
# driver.find_element(By.XPATH,"//span[@class='sbpqs_a']").click()
driver.find_element(By.XPATH,"//ytd-item-section-renderer[4]//div[3]//ytd-playlist-renderer[1]//div[1]//a[1]//h3[1]//span[1]").click()
time.sleep(5)


