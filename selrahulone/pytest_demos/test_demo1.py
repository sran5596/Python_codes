def test_fisrtone():
    print("this is my first test case")
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
driver=test_fisrtone()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
if driver.title=="Practice Page":
    print("pass")
else:
    print("fail")
driver.quit()