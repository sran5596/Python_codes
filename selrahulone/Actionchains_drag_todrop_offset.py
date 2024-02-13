from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
obj=Service("D:/drivers/chromedriver.exe")

chrm=webdriver.ChromeOptions()
chrm.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=obj)
mywait=WebDriverWait(driver,20)
driver.get("https://www.flipkart.com/mobile-phones-store")
chrm.add_argument("--disable-notifications")
id=driver.current_window_handle
print(id)
# if driver.switch_to.alert in id:
#     mywait.until(EC.alert_is_present((By.XPATH, "/html/body/div[3]/div/span"))).click()
# driver.switch_to.alert
# while True:
#     driver.switch_to.alert
#     driver.find_element(By.XPATH, "/html/body/div[3]/div/span").click()
# else:
#     time.sleep(5)

# alt=mywait.until(EC.alert_is_present((By.XPATH,'/html/body/div[3]/div/span')))
# alt=mywait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/span')))
# alt.click()

driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("mobiles")
time.sleep(5)
sea=mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
sea.click()
time.sleep(5)
min_slider=driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[1]/div")
max_slider=driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[2]/div")
print(min_slider.location)
print(max_slider.location)
time.sleep(5)
act=webdriver.ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
time.sleep(5)
act.drag_and_drop_by_offset(max_slider,-39,0).perform()
print("after moved slider location:...")
print(min_slider.location)
print(max_slider.location)


