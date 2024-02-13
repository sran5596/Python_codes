import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("abc")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@class='_9lsb _9ls8' or @class='_9lsb _9ls9']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[id='loginbutton']").click()
msg=driver.find_element(By.CSS_SELECTOR,"div[class='_9ay7']").text
print(msg)
assert "The email address or mobile number you entered isn't connected to an account" in msg



