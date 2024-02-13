from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
# id1=driver.current_window_handle
# print(id1)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
# id2=driver.current_window_handle
# print(id2)
# time.sleep(5)
ids=driver.window_handles
print(ids[0])
print(ids[1])
one=ids[0]
two=ids[1]
driver.switch_to.window(two)
print(driver.title)
# for li in ids: # getting the title of every one
#     driver.switch_to.window(li)
#     print(driver.title)

# for li in ids: #close the specific window
#     driver.switch_to.window(li)
#     if driver.title=="OrangeHRM":
#         driver.close()
# time.sleep(5)

for li in ids:
    driver.switch_to.window(li)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title=="OrangeHRM":
        driver.close()