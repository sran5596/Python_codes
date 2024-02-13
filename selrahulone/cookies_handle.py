from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
act=webdriver.ActionChains(driver)
driver.get("https://demo.nopcommerce.com/")
driver.add_cookie({"name":"Raveendra","value":"100crore"})
print(driver.get_cookies())
readone=Keys.CONTROL+Keys.ENTER
driver.find_element(By.XPATH,"//a[@class='ico-register']").send_keys(readone)
print(driver.get_cookies())
for c in driver.get_cookies():
    print(c.get("name"),":",c.get('value')) # ":" -concat symbol
driver.add_cookie({"name":"Raveendra","value":"100crore"})
for r in  driver.get_cookies():
    if "name"=="raveendra" and 'value'=="100crore":
        print(c.get("name"),":",c.get('value'))
# assert "Raveeendra" and "100crore" in driver.get_cookies()

driver.close()