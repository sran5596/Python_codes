from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(10)
driver.maximize_window()
#order
#first click the sort button and captuire the list
#capture the new sorted list
#compare the list it
second_list=[]
#without click the sort button on the webpage
# one_list=driver.find_elements(By.XPATH,"//table[@class='table table-bordered']/tbody/tr/td[1]")
# # one_list.sort()
# print(one_list)
# for i in one_list:
#     print(i.text)
#     second_list.append(i.text)
#     actual_lis=one_list
# second_list.sort()
# assert second_list==one_list
#click the soprt button
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div/table/thead/tr/th[1]/span[1]").click()
one_list = driver.find_elements(By.XPATH, "//table[@class='table table-bordered']/tbody/tr/td[1]")
# one_list.sort()
print(one_list)
for i in one_list:
    print(i.text)
    second_list.append(i.text)
    actual_list=second_list
second_list.sort()
assert second_list == actual_list
print(actual_list)
