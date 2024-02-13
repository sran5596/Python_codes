#xpath axis- and or contains(@id,st) starts-with(@id,st) text()='value'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/dailygroupa")
#self
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]").text)
elee=driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]")
print(elee.is_displayed())
#parent
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/parent::td").text)
#child
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/child::td").text)
cc=driver.find_elements(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/child::td")
print(len(cc))
# for i in cc:
#     print(i.get_attribute("text"))
#ancestor
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr").text)

#descendant
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/descendant::*").text)
#follow
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/following::*").text)
#following-sibling
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/following-sibling::*").text)
#preceding
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/preceding::*").text)
#preceding-sibling
print(driver.find_element(By.XPATH,"//a[contains(text(),'Tirupati Starch')]/ancestor::tr/preceding-sibling::*").text)
