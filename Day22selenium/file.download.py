from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
def chrome1():
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver import ChromeOptions
    ops=webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj,options=ops)
    driver.implicitly_wait(10)
    return driver

my_driver=chrome1()
my_driver.get("https://file-examples.com/")

brow=my_driver.find_element(By.XPATH,"//*[@id='features']/div/div[2]/div/div/div[1]/div[3]/div/a")


# my_driver.execute_script("arguments[0].scrollByView();",brow)
# one=my_driver.execute_script("return window.pageYOffset;")
# print("pixels of one:",one)
brow.click()
time.sleep(5)

two=my_driver.find_element(By.XPATH,"//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-doc-download/']")
# my_driver.execute_script("arguments[0].scrollByView();",two)
# value=my_driver.execute_script("retrun window.pageYOffset;")
# print("value pixels:",value)
two.click()
time.sleep(5)

three=my_driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]")
# my_driver.execute_script("arguments[0].scrollByView();",three)
# valuethree=my_driver.execute_script("return window.pageYOffset;")
# print("valuethree:",valuethree)
three.click()
time.sleep(5)