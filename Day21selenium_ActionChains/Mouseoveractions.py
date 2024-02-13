from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.LINK_TEXT," Login ").click()
#mouse over
admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b") #created the webele
usermanage=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")
act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermanage).move_to_element(users).click().perform()
#passed the above