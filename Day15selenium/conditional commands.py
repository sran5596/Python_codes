# # is_displayed()
# # is_enabled()
# # is_selected()
# #[[[imp]]]-its accessbul via object not driver
# #driver.is_displayed/is_selected/is_enabled its not works
#
# #[this elements is accessed via browser only]
#
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
d1=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[3]/fieldset[1]/input[1]")
print(d1.is_displayed())
print(d1.is_enabled())
#selected works on radio buttons only
# driver.find_element(By.XPATH,"//*[@id='checkbox-example']/fieldset/label[1]").click()
# driver.find_element(By.XPATH,"//*[@id='checkbox-example']/fieldset/label[1]").click()
driver.find_element(By.XPATH,"//input[@value='option1']").click()
b1=driver.find_element(By.XPATH,"//input[@value='option1']")

b2=driver.find_element(By.XPATH,"//input[@value='option2']")
b3=driver.find_element(By.XPATH,"//input[@value='option3']")
print(b1.is_selected())
print(b2.is_selected())
print(b3.is_selected())

#ststic
opt=Select(driver.find_element(By.XPATH,"//*[@id='dropdown-class-example']"))
opt.select_by_index(1)
time.sleep(5)
#time.sleep(5)
print(driver.title)
driver.close()

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/input[1]").send_keys("ind")
cou=driver.find_elements(By.CLASS_NAME,"ui-corner-all")
print(len(cou))
time.sleep(3)
for li in cou:
    print(li.text)
    if li.text == "India":
        li.click()
        break
#print(driver.find_element(By.CLASS_NAME,"ui-corner-all").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value")== "India"