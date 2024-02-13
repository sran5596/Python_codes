from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #its used for explicitwait
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#che=driver.find_elements(By.CLASS_NAME,"form-check-label") #i am written
che=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(che))

#Apporach-1
# for list in range(len(che)): # it select all items
#     che[list].click()

#Apporach2
# for list in che: # selecting all items at a time
#     list.click()

# # #Apporach3
try:
    for list in che: # selecting the monday and sunday week
        weekname=list.get_attribute('id')
        if weekname=="Monday" or weekname=='Sunday':
            list.click()
        time.sleep(5)

except Exception as e:
    print(e)
# time.sleep(5)
#Apporach4
# for check in range(len(che)-2,len(che)): #selecting the last two
#         che[check].click()

#Apporach5
# for ch in range(len(che)): #its selecting the first two elemenets
#     if ch<2:
#         che[ch].click()

#Apporach6
# for check in che:
#     check.is_selected()
#     check.click()




