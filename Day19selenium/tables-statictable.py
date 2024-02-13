#1)count of the total no of rows and columns
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
rows=len(driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr"))
# print(len(rows))
print(rows)
columns=len(driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[1]/td"))
print(columns)
# print(len(columns))

#read the specifi row and column in table
eng=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[5]/td[2]").text
print(eng)

#3)read the all rows and column data
for r in range(1,rows+1):
    for c in range(1,columns+1):
        data=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[' +str(r)+ ']/td[' +str(c)+ ']").text
        print(data,end="   ")
    print()

#4)read the data based on condition
for r in range(1,rows+1):
    position=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[' +str(r)+ ']/td[2]").text
    if position=="Engineer":
        name=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr/td[1]").text
        city=driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr/td[3]").text
        print(name, "   " ,city)


