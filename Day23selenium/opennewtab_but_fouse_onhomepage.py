#mouse operation this is also
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# open the new tab using the ctrl+Enter
buttons=Keys.CONTROL+Keys.ENTER #it store the [ctrl+Enter]
#below find element and give the send_keys(buttons) it open the new tab but foucs on the homepage
driver.find_element(By.XPATH,"//a[@class='ico-register']").send_keys(buttons)
time.sleep(5)
#open the new tabs
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('tab') #it open the new tab
driver.get("https://ww1.ibomma.link/telugu-movies/")
#open the twe different browsers
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('window') #it open the new tab
driver.get("https://ww1.ibomma.link/telugu-movies/")