import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=object)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# #singele element-find_element used
# driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("abwtyfchsgouj")
#find_elements use
driver.get("https://demo.nopcommerce.com/")
li1=driver.find_elements(By.XPATH,"/html/body/div[6]/div[4]/div[1]")
print(len(li1))
#identify the meluiple elements
li11=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(li1))
print(li11[0].text)
for y in li11:
    print(y.text)
time.sleep(5)
driver.maximize_window()
print(driver.title)
driver.close()