from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def cookies():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
driver=cookies()
driver.get("https://demo.nopcommerce.com/")
clist=driver.get_cookies()
print(len(clist))
for i in clist:
    print(i)
driver.delete_all_cookies() #its delete all cookies
driver.delete_cookie("key") # its delete the particular key
print(i.get("sameSite"),":",i.get(".Nop.Customer"),i.get("expiry")) # retrive the cookies
#driver.add_cookie({'name':'Mycookie'}) # its adding new cookie for your side
driver.delete_cookie("Lax")

clist1=driver.get_cookies()
print(len(clist1))
driver.quit()