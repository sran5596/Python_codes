# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# mywait=WebDriverWait(driver,10,poll_frequency=2)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # radio=mywait.until(EC.presence_of_element_located((By.XPATH,"//label[@for='radio1']")))
# # time.sleep(2)
# # radio.click()
# driver.find_element(By.XPATH,"//label[@for='radio1']").click()
# time.sleep(2)
# # print(radio.text)
import requests
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR,"label[for='radio3']").click()
# time.sleep(2)

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radiobuttons=driver.find_elements(By.XPATH,"//input[@class='radioButton' and @name='radioButton']")
# print(len(radiobuttons))
# for i in radiobuttons:
#     print(i.get_attribute('value'))
#     if i.get_attribute('value')=='radio1':
#         i.click()
# # time.sleep(2)
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# items=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
# print(len(items))
#selecting the all or needed ones only
# for i in items:
#     print(i.get_attribute('value'))
#     # i.click()
#     if i.get_attribute('value')=='option1' or i.get_attribute('value')=='option3':
#         i.click()

#last one seelcting
#usd te range function
# for i in range(len(items)-1,len(items)):
#     items[i].click()

#first one selecting
# index used
# for i in range(len(items)):
#     if i<1:
#         items[i].click()
# time.sleep(2)

#links-internal & external & broken
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)
# links=driver.find_elements(By.TAG_NAME,'a')
# print(len(links))
# for i in links:
#     print(i.get_attribute('href'))
#     if i.get_attribute('href')=='https://www.qaclickacademy.com/':
#         i.click()
# time.sleep(2)
# print(driver.title)

# #Broken links handle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("http://www.deadlinkcity.com/")
# linksall=driver.find_elements(By.TAG_NAME,'a')
# print(len(linksall))
# count=0
# for i in linksall:
#     url=i.get_attribute('href')
#     try:
#         res=requests.head(url)
#     except Exception as e:
#         print(e)
#     if res.status_code>=400:
#         print(url ,"url is broken link")
#         count+=1
#     else:
#         print(url ,"is valid link")
# print('Total no if links :', count)










