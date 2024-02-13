# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# def hrm_one():
#     obj=Service("D:/drivers/msedgedriver.exe")
#     driver=webdriver.Edge(service=obj)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     # mywait=WebDriverWait(driver,10)
#     return driver
# new_driver=hrm_one()
# new_driver.get("https://opensource-demo.orangehrmlive.com/")
# print(new_driver.title)
# new_driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# new_driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# new_driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# print(new_driver.current_url)
# print(new_driver.session_id)
# new_driver.get_cookies()
# print(new_driver.page_source)
# new_driver.quit()




