from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
# def brohan():
#     obj=Service("D:/drivers/msedgedriver.exe")
#     driver=webdriver.Edge(service=obj)
#     driver.get("https://demo.nopcommerce.com/")
#     driver.maximize_window()
#     ele=driver.find_element(By.XPATH,"//a[normalize-space()='Facebook']")
#     driver.execute_script("arguments[0].scrollIntoView();",ele)
#     time.sleep(5)
#     print(driver.current_window_handle)
#
# brohan()

#multiple
def brohan1():
    obj=Service("D:/drivers/msedgedriver.exe")
    driver=webdriver.Edge(service=obj)
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    ele=driver.find_element(By.XPATH,"//a[normalize-space()='Facebook']")
    driver.execute_script("arguments[0].scrollIntoView();",ele)
    time.sleep(5)
    ele.click()
    # print(driver.title)
    driver.find_element(By.XPATH,"//a[normalize-space()='Twitter']").click()
    # print(driver.title)
    driver.find_element(By.XPATH,"//a[normalize-space()='YouTube']").click()
    # print(driver.title)
    wids=driver.window_handles
    first=wids[0]
    sec=wids[1]
    thi=wids[2]
    fou=wids[3]
    for i in wids:
        driver.switch_to.window(i)
        print(driver.title)
        if driver.title=="nopCommerce - YouTube" :
            driver.close()
            break
    time.sleep(5)


brohan1()
