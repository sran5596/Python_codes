from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
driver=chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print(driver.title)
print(driver.current_url)
if driver.title=="OrangeHRM":
    print("yess")
else:
    print("noo")