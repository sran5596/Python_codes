#static table
#dynamic table
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj,options=ops)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# #counting the total rows and total columns
numberofrows=len(driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tr"))
print(numberofrows)
numberofcolumns=len(driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tr[1]//th"))
print(numberofcolumns)
# #read the specfic row and column data mena 3row-4column
# ele=driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tr[3]/td[4]")
# print(ele.text)
#read all data use of for loop
# for r in range(2,numberofrows+1):
#     for c in range(1,numberofcolumns+1):
#         data=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[' +str(r)+ ']/td[' +str(c)+ ']").text
#         print(data,end='')
#     print()

#list the people who belongs to chennai
for r in range(2,numberofrows+1):
    loc=driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tr["+str(r)+"]//td[3]").text
    if loc=="Chennai":
        name=driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tr["+str(r)+"]//td[1]").text
        position=driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tr["+str(r)+"]//td[2]").text
        age=driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tr["+str(r)+"]//td[4]").text
        print(loc," ",name," ",position," ",age)


