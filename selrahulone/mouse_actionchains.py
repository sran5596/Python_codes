import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
obj=Service("D:/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
act=webdriver.ActionChains(driver)
one=webdriver.ChromeOptions()
one.add_argument("--disable-notifications")
my=WebDriverWait(driver,10)
driver.get("https://www.orangehrm.com/en/orangehrm-starter-open-source-software/")
driver.maximize_window()
time.sleep(5)
r1=driver.find_element(By.XPATH,"//a[@class='nav-link-hed'][normalize-space()='Solutions']")
r2=driver.find_element(By.XPATH,"//body/nav[@class='navbar navbar-expand-lg navbar-light fixed-top']/div[@class='container-fluid']/div[@id='navbarSupportedContent']/ul[@class='navbar-nav me-auto mb-2 mb-lg-0 web-menu']/li[@class='nav-item']/div[@class='secondary']/div[@class='col-md-12 col-lg-12']/div[@class='sub-menu']/div[@class='secondary-menu']/ul/li[1]")
r3=driver.find_element(By.XPATH,"//div[@class='mob-list-section']//a[normalize-space()='Employee Management']")
time.sleep(5)
act.move_to_element(r1).move_to_element(r2).move_to_element(r3).click().perform()
time.sleep(1)
