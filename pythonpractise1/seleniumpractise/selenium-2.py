from selenium import webdriver
from selenium.webdriver.common.by import By
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\\drivers\\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
driver=chrome()
driver.get("https://www.facebook.com/signup/")
exp_title=driver.title
act_title="Sign up for Facebook | Facebook"
if exp_title==act_title:
    print("test passed")
else:
    print("test failed")