# self
# parent
# child
# ancester
# descedent
# preceding
# preceding-sibiling
# following
# following sibiling
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://money.rediff.com/gainers/bse/dailygroupa")
self=driver.find_element(By.XPATH,"//*[contains(text(),'AAA Technologies')]/self::a").text
parent=driver.find_element(By.XPATH,"//*[contains(text(),'AAA Technologies')]/parent::td").text
child=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/child::td")
ancestor=driver.find_element(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr").text
descendant=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/descendant::*")
following=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/following::*")
followingsibling=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/following-sibling::tr")
pre=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/preceding::tr")
print("list of pre :",len(pre))
presib=driver.find_elements(By.XPATH,"//*[contains(text(),'AAA Technologies')]/ancestor::tr/preceding-sibling::tr")
print("list of pre-sibling:",len(presib))
print("list of fol-sibling:",len(followingsibling))
print("list of following details:",len(following))
print("Descendant list is:",len(descendant))
print("ancestor list is:",ancestor)
print("childs list is:",len(child))
print("parent name is :",parent)
print("self name is :",self)

