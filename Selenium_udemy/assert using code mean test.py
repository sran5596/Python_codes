
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://www.instagram.com/accounts/login/")
#time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("abc") #css not working here
#driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("abc") # relational XPATH NOT
#driver.find_element(By.NAME,"username").send_keys("abc") # NAMe also not worked here
#driver.find_element(By.CSS_SELECTOR,"input._aa4b[name='username']").send_keys("abc") # its also not worked
#driver.find_element(By.CSS_SELECTOR,"input[aria-label='Phone']").send_keys("abc") #not
#driver.find_element(By.XPATH,"//*[@name='username' and @class='_aa4b _add6 _ac4d']").send_keys("abc")#not
# driver.find_element(By.XPATH,"(//input[@name='username'])[1]").send_keys("abc") #NOT
#driver.find_element(By.CSS_SELECTOR,"input._aa4b._add6._ac4d[name='username']") # NOt
#driver.find_element(By.XPATH,"//*[contains(@name,'username')]")#NOt
#time.sleep(3)
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("abc")
# time.sleep(5)
# driver.find(By.XPATH,"//*[text()='SHOW' or 'HIDE']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
# time.sleep(5)
# msg=driver.find_element(By.CSS_SELECTOR, "p[id='slfErrorAlert']").text
# print(msg)
# assert "Sorry" in msg


try:
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    obj = Service("D:\drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=obj)
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@name='username']").send_keys("abcUYJKGVIUKJ")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("abcYHATJYFCGIUSKJ")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@class='_acan _acao _acat _aj1-']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@class='_acan _acao _acat _aj1-']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()
    time.sleep(7)
    msg=driver.find_element(By.XPATH,"//p[@id='slfErrorAlert']").text
    print(msg)
    assert "Sorry, your password was incorrect. Please double-check your password." in msg
except Exception as e:
    print(e)

