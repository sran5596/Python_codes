from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://text-compare.com/")
mywait=WebDriverWait(driver,20)
one=webdriver.ChromeOptions()
act=webdriver.ActionChains(driver)
one.add_argument("--disable-notifications")
scrl=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
driver.execute_script("arguments[0].scrollIntoView();",scrl)
textone=mywait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='inputText1']")))
# textone=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
texttwo=mywait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='inputText2']")))
textone.send_keys("Raveendra")
#selecting all the words
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
#copy the text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
#pressing the TAB
act.key_down(Keys.TAB)
act.perform()
#paste the code
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
