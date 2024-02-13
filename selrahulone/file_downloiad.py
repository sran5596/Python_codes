from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def chrome1():
    obj = Service("D:/drivers/chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=obj, options=ops)
    return driver


my_driver = chrome1()
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.maximize_window()
my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
#my_driver.execute_script("arguments[0].scrollIntoView();", ele)
#ele.click()
time.sleep(5)

