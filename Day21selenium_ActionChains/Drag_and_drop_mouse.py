
#Used the Actionchains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

one_source=driver.find_element(By.XPATH,"//*[@id='box4']")
one_tar=driver.find_element(By.XPATH,"//*[@id='box106']")
act=ActionChains(driver)
act.drag_and_drop(one_source,one_tar).perform()
time.sleep(3)

two=driver.find_element(By.XPATH,"//*[@id='box5']")
twosource=driver.find_element(By.XPATH,"//*[@id='box101']")
act.drag_and_drop(two,twosource).perform()
time.sleep(3)

three=driver.find_element(By.XPATH,"//*[@id='box6']")
threesource=driver.find_element(By.XPATH,"//*[@id='box105']")
act.drag_and_drop(three,threesource).perform()
time.sleep(3)

four=driver.find_element(By.XPATH,"//*[@id='box7']")
foursource=driver.find_element(By.XPATH,"//*[@id='box103']")
act.drag_and_drop(two,twosource).perform()
time.sleep(3)

five=driver.find_element(By.XPATH,"//*[@id='box1']")
fivesource=driver.find_element(By.XPATH,"//*[@id='box107']")
act.drag_and_drop(four,foursource).perform()
time.sleep(3)

six=driver.find_element(By.XPATH,"//*[@id='box2']")
sixsource=driver.find_element(By.XPATH,"//*[@id='box104']")
act.drag_and_drop(five,fivesource).perform()
time.sleep(3)

seven=driver.find_element(By.XPATH,"//*[@id='box3']")
sevensource=driver.find_element(By.XPATH,"//*[@id='box102']")
act.drag_and_drop(six,sixsource).perform()
time.sleep(3)