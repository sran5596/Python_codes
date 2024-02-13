# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# tit="nopCommerce demo store"
# exp_tit=driver.title
# if tit==exp_tit:
#     print("yes")
# assert tit==driver.title
#driver.quit

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https:https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").clear()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//input[@placeholder='Username']").clear()
# # # time.sleep(2)
# # driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# # time.sleep(2)
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").clear()
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# # driver.find_element(By.XPATH,"//input[@placeholder='Password']").clear()
# # driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# tit1=driver.title
# print(tit1)
# if tit1=="OrangeHRM":
#     print("yes")
#     raise Exception("Exception is good ")
# assert "HRM" in tit1
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
# # obj=Service("D:\drivers\chromedriver.exe")
# obj=Service("D:\drivers\msedgedriver.exe")
# # driver=webdriver.Chrome(service=obj)
# driver=webdriver.Edge(service=obj)
# driver.get("https://admin-demo.nopcommerce.com/login")
# driver.find_element(By.XPATH,"//*[@id='Email']").clear()
# driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH,"//*[@id='Password']").clear()
# driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("admin")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# print(driver.title)
# actital="Dashboard / nopCommerce administration"
# expected=driver.title
# if expected==actital:
#     raise Exception("its goood")
# assert "no" in expected

