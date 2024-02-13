from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# def dropdowns():
#     obj=Service("D:\drivers\msedgedriver.exe")
#     driver=webdriver.Edge(service=obj)
#     driver.implicitly_wait(10)
#     return driver
# driver=dropdowns()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# time.sleep(5)
# # mywaut=WebDriverWait(driver,10)
# # mywaut.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='dropdown-class-example']")))
# items=Select(driver.find_element(By.XPATH,"//*[@id='dropdown-class-example']"))
# one=items.select_by_visible_text("Option3")
# time.sleep(5)
# driver.quit()
# def static_dropdowns():
#     obj=Service("D:\drivers\msedgedriver.exe")
#     driver=webdriver.Edge(service=obj)
#     driver.implicitly_wait(10)
#     return driver
# driver=static_dropdowns()
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.XPATH,"//*[@id='autosuggest']").send_keys("ind")
# list=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']//li")
# print(len(list))
# for i in list:
#     print(i.text)
#     if i.text=="India":
#
#         i.click()
#
#
#         break
# time.sleep(5)
# driver.quit()
obj=Service("D:\drivers\msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.implicitly_wait(10)
driver.get("https://money.rediff.com/gainers/bse/dailygroupa")
driver.execute_script("window.scrollBy(0,1000)","")
print(driver.execute_script("return window.pageYOffset;",))
item=driver.find_element(By.XPATH,"//a[normalize-space()='MCX']")
driver.execute_script("arguments[0].scrollIntoView();",item)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)
