# get/application commands
# get,title,current_url,page source code
# conditional commands
# is_selected,is_enabled,is_selected
# browser commands
#close,quit
# navigational commands
# back(),forward,refresh
# wiat commands

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)

#get/application commands example
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)

#conditional commnads
# rd1=driver.find_element(By.XPATH,"//*[@value='radio1' and @name='radioButton']")
# rd1.click()
# print(rd1.is_displayed())
# print(rd1.is_enabled())
# print(rd1.is_selected())

# browser commands
# driver.get("https://money.rediff.com/gainers/bse/dailygroupa")
# driver.back()
# print(driver.title)
# driver.forward()
# print(driver.title)
# driver.refresh()
#
# driver.close()
#driver.quit()

#Differnece between the find elements
# driver.get("https://demo.nopcommerce.com/")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.implicitly_wait(10)
#find_element
# search=driver.find_element(By.CSS_SELECTOR,"input[type='text']")
# search.send_keys("phone")
# time.sleep(2)
#find_elements
# li=driver.find_elements(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[2]/ul/li/a")
# li=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(li))
# for i in li:
#     print(i[1].text)
# li=driver.find_elements(By.XPATH,"//table[@class='gf-t']//a")
# # print(len(li))
# print(li[4].text)
# for i in li:
#     # print(i.text)
#     if i.text=='SoapUI':
#         i.click()
# time.sleep(5)


#text and get attribute
# s=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
# s.send_keys("heroo")
# # print(s.text)
# print(s.get_attribute('value'))
# time.sleep(5)
# one=driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a")
# print(one.text)

#wait commands
# impli
# explicity
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.implicitly_wait(10)
# driver.get("https://www.google.com")
# sea=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
# sea.send_keys("iphone")
# print(sea.get_attribute('value'))

#Explicitwait
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# mywait=WebDriverWait(driver,10)
# driver.get("https://www.google.com")
# search=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
# search.send_keys("selenium")
# search.get_attribute('value')
# search.submit()
# sel=mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")))
# print(sel.text)
# sel.click()

#Explicit
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# mywait=WebDriverWait(driver,10,poll_frequency=5)
# driver.get("https://www.google.com")
# search=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
# search.send_keys("python")
# search.get_attribute('value')
# search.submit()
# pyt=mywait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/div/span/a/h3")))
# pyt.click()
# print(driver.title)

