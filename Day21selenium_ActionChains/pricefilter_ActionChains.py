from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax")
min_slider=driver.find_element(By.XPATH,"//div[@class='_31Kbhn _28DFQy']//div[@class='_3FdLqY']")
max_slider=driver.find_element(By.XPATH,"//div[@class='_31Kbhn WC_zGJ']//div[@class='_3FdLqY']")
print("location of the sliders..")
print(min_slider.location)
print(max_slider.location)
act=ActionChains(driver)
print("location of the after done ...")
act.drag_and_drop_by_offset(min_slider,100,0).perform() # sir given used to filter the min and max values
act.drag_and_drop_by_offset(max_slider,-50,0).perform()
time.sleep(5)
print(min_slider.location)
print(max_slider.location)
one=Select(driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select"))
one.select_by_value("15000")
two=Select(driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select"))
two.select_by_value("20000")
time.sleep(5)