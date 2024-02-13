#import the action cahins
#mouse over-move_to_element
#right_click()-context_clikc()
#double_click()

#drag_and_drop()-source and target
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
obj=Service("D:/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
mywait=WebDriverWait(driver,20)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
# opt.add_argument("--disable-notifications")
act=ActionChains(driver)
admin=mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
admin.send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
pas=mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']")))
pas.send_keys("admin123")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(4)
# opt.add_argument("--disable-notifications")
one=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
one.click()
two=mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li/ul/div[1]/li/a")))
two.click()
third=mywait.until(EC.presence_of_element_located((By.XPATH,"//ul[@role='menu']//li")))
# one.click()
# act.move_to_element(two).move_to_element(third).click().perform()
# time.sleep(5)
third.clik()
time.sleeep(5)
