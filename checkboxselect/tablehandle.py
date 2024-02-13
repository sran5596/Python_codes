from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
obj=Service("D:/driveers/msedgedriver.exe")
ops=webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Edge(service=obj,options=ops)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
one=driver.find_element(By.XPATH,"//th[normalize-space()='Name']")
driver.execute_script("arguments[0].scrollIntoView();",one)
rows=len(driver.find_elements(By.XPATH,"//table[@id='product']/tbody/tr"))
print(rows)
columns=len(driver.find_elements(By.XPATH,"//table[@id='product']/tbody/tr[1]/td"))
print(columns)
#reda specific data
print(driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr[3]/td[2]").text)

#read all data from the table
for r in range(2,rows+1):
    for c in range(1,columns+1):
        data=driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)