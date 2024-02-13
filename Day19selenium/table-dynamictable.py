from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
one=webdriver.ChromeOptions()
one.add_argument("--disable-notifications")
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
lists=driver.find_elements(By.XPATH,"//div[@class='oxd-table-body oxd-card-table-body']/div/div")
print(len(list))
time.sleep(5)
#sir given code is
count=0 #for counting the total
for r in range(1,lists+1):
    status=driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status=="Enable":
        count+=1
        print("total number of users:" ,lists)
        print("numbers of enables",count)
        print("number os disable",(lists-count))
driver.close()

