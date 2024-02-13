from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
obj=Service("D:/drivers/msedgedriver.exe")
driver=webdriver.Edge(service=obj)
driver.maximize_window()

act=ActionChains(driver)
#below code for move_to_element
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//input[@placeholder='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# mywait=WebDriverWait(driver,20)
# mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"Admin"))).click()
# mywait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='Organization']//i[@class='oxd-icon bi-chevron-down']"))).click()
# one=driver.find_element(By.XPATH,"//a[normalize-space()='Structure']")
# act.move_to_element(one).click().perform()
# time.sleep(5)
#right
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# button=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
# act.context_click(button).perform()
# time.sleep(5)
# driver.find_element(By.XPATH,"/html/body/ul/li[7]/span").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# time.sleep(5)
#darg ans drop
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# ele=driver.find_element(By.XPATH,"//div[@id='box4']")
# source=driver.find_element(By.XPATH,"//div[@id='box101']")
# act.drag_and_drop(ele,source).perform()
# time.sleep(5)

#sliders
# driver.get("https://www.flipkart.com/mobile-phones-store")
# min_slide=driver.find_element(By.XPATH,"//div[@class='_31Kbhn _28DFQy']//div[@class='_3FdLqY']")
# driver.execute_script("arguments[0].scrollIntoView();",min_slide)
# print(min_slide.location)
# max_slide=driver.find_element(By.XPATH,"//div[@class='_31Kbhn WC_zGJ']//div[@class='_3FdLqY']")
# print(max_slide.location)
# act.drag_and_drop_by_offset(min_slide,100, 0).perform()
# act.drag_and_drop_by_offset(max_slide,-39, 0).perform()
# print(min_slide.location)
# print(max_slide.location)
# time.sleep(5)

#scrolling - based on element
driver.get("https://www.flipkart.com/mobile-phones-store")
# ele=driver.find_element(By.XPATH,"//a[normalize-space()='About Us']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# print(driver.execute_script("return window.pageYOffset;"))
#based on fixel
# driver.execute_script("window.scrollBy(0,300)","")
# time.sleep(5)
#total down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(2)
#scroll top
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))
time.sleep(2)