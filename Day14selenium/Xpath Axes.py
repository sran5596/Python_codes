# self
# parent
# child
# ancestor
# descendant
# following nodes
# following-sibling
# preceding
# preceding-sibling

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://money.rediff.com/gainers/bse/dailygroupa")
#self element
self_ele=driver.find_element(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/self::a").text
print(self_ele)
#parent
par_ele=driver.find_element(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/parent::*").text
print(par_ele)
#child
child_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::*/child::*")
print(len(child_ele))
#ancestor
ane_ele=driver.find_element(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr").text
print(ane_ele)
#descendant
de_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr/descendant::td")
print(len(de_ele))
#preceding
pre_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr/preceding::*")
print(len(pre_ele))
#preceding-sibling
pre_sli_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr/preceding-sibling::*")
print(len(pre_sli_ele))
#following
flow_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr/following::*")
print(len(flow_ele))
#following-sibling
fol_sib_ele=driver.find_elements(By.XPATH,"//*[contains(text(),'Eureka Forbes')]/ancestor::tr/following-sibling::*")
print(len(fol_sib_ele))
driver.quit()