from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
buttons=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(buttons))
#a==all select at atime
# for one in range(len(buttons)):
#     buttons[one].click()
# time.sleep(5)
#a-2==all select
# for one in buttons:
#     one.click()
#a-3==specifc select
for one in buttons:
    #week=one.get_attribute("id")
    #if week=="Monday" or week=="Sunday":
    if one.get_attribute("id")=="MOnday":
        one.click()
time.sleep(5)
#a-4 -- select last three
# for one in range(len(buttons)-3,len(buttons)): # 7-3=4-start index and end index=7
#     buttons[one].click()
# time.sleep(5)
#a-4= select the first three use logic
# for one in range(len(buttons)):
#     if one<3:
#         buttons[one].click()
# time.sleep(5)
#a-5  used conditional commands-is_displayed,is_enabled,is_selected
# for one in buttons:
#     one.is_selected()
#     one.click()
# time.sleep(5)