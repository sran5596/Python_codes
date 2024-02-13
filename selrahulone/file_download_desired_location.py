from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os #it give the currenet working directory
location=os.getcwd()
def chrome1():
    obj=Service("D:/drivers/chromedriver.exe")
    # driver=webdriver.Chrome(service=obj)
    # preferences={"download.default_directory":"D:\\filehandlefolder"} #its for need ed location
    preferences = {"download.default_directory": location}
    chr=webdriver.ChromeOptions()
    chr.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=obj,options=chr)
    return driver
one=chrome1()
one.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
mywait=WebDriverWait(one,10)
mywait.until(EC.presence_of_element_located((By.XPATH,"//tbody/tr[1]/td[5]/a[1]"))).click()
# one.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)