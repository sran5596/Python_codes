# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# obj=Service("D:/drivers/msedgedriver.exe")
# driver=webdriver.Edge(service=obj)
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
# # driver.switch_to.alert.accept()
# time.sleep(2)
# # driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
# # po=driver.switch_to.alert
# # po.dismiss()
# # time.sleep(2)
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# pop=driver.switch_to.alert
# time.sleep(5)
# pop.send_keys("Shiva")
# print(pop.text)
# time.sleep(5)

# #authonication popups
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# obj=Service("D:/drivers/msedgedriver.exe")
# driver=webdriver.Edge(service=obj)
# driver.maximize_window()
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# print(driver.find_element(By.XPATH,"//*[@id='content']/div/p").text)
# time.sleep(2)
