#Relatve Xpatrh-//tagname
#absolutive Xpath-/html
#classname
#linked text
#partial link text
#id
#name

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
# obj=Service("D:\drivers\chromedriver.exe")
# # obj=Service("D:\drivers\msedgedriver.exe")
# driver=webdriver.Chrome(service=obj)
# # driver=webdriver.Edge(service=obj)
# # driver.get("https://admin-demo.nopcommerce.com/login")
# driver.get("https://www.amazon.in/")
#id
# driver.find_element(By.ID,"Email").clear()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
#name
# driver.find_element(By.NAME,"Email").clear()
# driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
#Linked text
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,"Log in").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
# time.sleep(2)
#Classname
# clist=driver.find_elements(By.CLASS_NAME,"inputs")
# print(len(clist))
# for i in clist:
#     print(i.text)
#Tagname
# tlist=driver.find_elements(By.TAG_NAME,"buttons")
# print(len(tlist))
# clist=driver.find_elements(By.CLASS_NAME,"a-carousel-card")
# print(len(clist))
# for i in clist:
#     print(i.text)
# clist=driver.find_elements(By.TAG_NAME,"li")
# print(len(clist))
# for i in clist:
#     if i.text=="Careers":
#         continue
#     print(i.text)
# assert "careers" not in print(i.text)
# print(len(driver.find_elements(By.TAG_NAME,"img")))

