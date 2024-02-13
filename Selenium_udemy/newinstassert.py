import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj = Service("D:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@name='username']").send_keys("abcUYJKGVIUKJ")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("abcYHATJYFCGIUSKJ")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='_acan _acao _acat _aj1-']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='_acan _acao _acat _aj1-']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()
time.sleep(2)
msg=driver.find_element(By.XPATH,"//p[@id='slfErrorAlert']").text
print(msg)
msg=="Sorry, your password was incorrect. Please double-check your password."
if msg=="Sorry, your password was incorrect. Please double-check your password.":
    pass
    #raise Exception("oky")
assert(msg=="Sorry, your password was incorrect. Please double-check your password.")