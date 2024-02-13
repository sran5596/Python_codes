from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://text-compare.com/")
one=driver.find_element(By.XPATH,"//*[@id='inputText1']")
two=driver.find_element(By.XPATH,"//*[@id='inputText2']")
act=ActionChains(driver)

#used to just pixel go down
# driver.execute_script("window.scrollBy(0,2000)","")
# value=driver.execute_script("return window.pageYOoffset;")
# print("value of the pixel:",value)

#used the field to go down
driver.execute_script("arguments[0].scrollIntoView();",one)
value=driver.execute_script("return window.pageYOffset;")
print("pixels:",value)
one.send_keys("Hai Raveendra Your total income in one year is 150 crores")
#click the ctrl+a used the keyboard
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
#or
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#Use the CTRl+V
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
#or
#act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

#use the TAB here
act.key_down(Keys.TAB)
act.key_up(Keys.TAB)

#use the CTrl+v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
#or
#act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)