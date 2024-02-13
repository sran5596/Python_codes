#TAG AND ID -- SYNTAX -- tagname#id--ex--input#email
#TAG AND CLASS -- SYNTAX -- tagname.valueofclass--ex--input.inpetext
#TAG AND ATTRIBUTE -- SYNTAX -- tagname[attribute=value] --ex--input[data="valuie]
#TAG AND CLASS ATTRIBUTES -- SYNTAX -- tagname.valueofclass[attribute=value of attribute]--ex--input.input[data=email]

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
#TAG#ID
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")
# time.sleep(3)

#TAG.VALUEOFCLASS
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")
# time.sleep(3)

#TAG[ATTRIBUTE=VALUE OF ATTRIBUTE]
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.CSS_SELECTOR,"input[autocomplete='username']").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"[autocomplete='username']").send_keys("abc")
# time.sleep(3)

#TAG.CLASSVALUE[ATTRIBUTE=ALOFATTRIBUTE]
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[aria-label='Password']").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,".inputtext[aria-label='Password']").send_keys("abc")
# time.sleep(3)

# TAG_NAME ex
# driver.get("https://www.flipkart.com/")
# link=driver.find_elements(By.TAG_NAME,"a")
# print(type(link))
# print(len(link))

#CLASS_NMAE EX
# driver.get("https://automationpractise.com/index.php")
# link=driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print(type(link))
# print(len(link))

