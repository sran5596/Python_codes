from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
obj=Service("D:/drivers/msedgedriver.exe")
import time
driver=webdriver.Edge(service=obj)
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.XPATH,"//body/form[@id='aspnetForm']/div[@class='maincontainer']/div[@id='wrapper']/div[@id='mainContents']/div[@id='new-homepage']/div[@id='home_banner']/div[@class='home_flight_search']/div[@id='content-change']/div[@class='book']/div[@id='flightSearchContainer']/div[@class='picker-first2']/button[1]").click()
# time.sleep(5)
# days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# for i in days:
#     if i.get_attribute('ui-datepicker-div')=="19":
#
#         i.click()
#         print(i.get_attribute('ui-datepicker-div'))
#         print(i.text)
#         break(
# time.sleep(5)
mywait=WebDriverWait(driver,10,poll_frequency=10,ignored_exceptions=[NoSuchElementException,StaleElementReferenceException,ElementNotInteractableException,ElementClickInterceptedException])
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
fr=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
mywait.until(EC.frame_to_be_available_and_switch_to_it(fr))
# driver.switch_to.frame(fr)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
month,year,date='June','2022','14'
while True:
    mn=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mn==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()
days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for day in days:
    if day.text==date:
        day.click()

        break

print(driver.find_element(By.XPATH,"//*[@id='datepicker']").get_attribute("datepicker"))
time.sleep(6)

