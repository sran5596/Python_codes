#ABSOLUTE_xpath-- STATRS WITH - /html/body/.....
#Relative_XPATH -- start with DOM elemunt --//tagname[@attribute="value of attribute"]

#XPATH Options
# or
# and
# contains() [[[mostimp]]] if button have two function like login and logout that case use his
#starts-with()
#text()


# class X1:
#
#     def xp1(self):
#         import time
#         from selenium import webdriver
#         from selenium.webdriver.chrome.service import Service
#         from selenium.webdriver.common.by import By
#         obj=Service("D:\drivers\chromedriver.exe")
#         driver=webdriver.Chrome(service=obj)
#         driver.maximize_window()
#         driver.get("https://www.facebook.com/login/")
#         #driver.get("https://automationpractise.com/index.php")
#         #driver.get("https://www.flipkart.com/")
#
#         # #identify the element using id
#         # driver.find_element(By.ID,"email").send_keys("anc")
#         #
#         # #Identify the element using NAME
#         # driver.find_element(By.NAME,"pass").send_keys("abc")
#         #
#         # #Identify the element using the LINKED_TEXT
#         # driver.find_element(By.LINK_TEXT,"Forgotten").click()
#         # driver.back()
#
#         #Identify the element using partial_linked_text
#         # driver.find_element(By.PARTIAL_LINK_TEXT,"Forg").click()
#
#         #Identify the element using CLASS_NAME
#         # slides = driver.find_elements(By.CLASS_NAME, "homeslider-container")
#         # print(type(slides))
#         # print(len(slides))
#
#         # Identify the element using TAG_NAME
#         # link=driver.find_elements(By.TAG_NAME,"a")
#         # print(len(link))
#
#         #CSS_selectors use to find elements
#         # driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc") # tagname#id
#         # driver.find_element(By.CSS_SELECTOR, "input#email").clear()
#         # driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc") # tagname.value of class
#         # driver.find_element(By.CSS_SELECTOR, "input.inputtext").clear()
#         # driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']").send_keys("abc")
#         # driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']").clear()
#         # driver.find_element(By.CSS_SELECTOR, "input.inputtext[autocomplete='username']").send_keys("abc")
#         # driver.find_element(By.CSS_SELECTOR, "input.inputtext[autocomplete='username']").clear()
#
#         #usiong the absolute XPATH
#         # driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input").send_keys("abc")
#         # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input").clear()
#         #
#         # #using the relational XPATH
#         # driver.find_element(By.XPATH,"//*[@id='email']").send_keys("abc")
#         # driver.find_element(By.XPATH,"//*[@id='email']").clear()
#
#         #XPATH OPTIOPNS USED TO FIND ELEMNTER
#         # driver.find_element(By.XPATH,"//*[@id='email' or @tabindex='0']").send_keys("abc") #or used
#         # driver.find_element(By.XPATH, "//*[@id='email' or @tabindex='0']").clear()
#         # driver.find_element(By.XPATH, "//*[@id='email' and @tabindex='0']").send_keys("abc") #and used
#         # driver.find_element(By.XPATH, "//*[@id='email' and @tabindex='0']").clear()
#         # driver.find_element(By.XPATH,"//*[contains(@id,'em')]").send_keys("abc") #contains() used
#         # driver.find_element(By.XPATH, "//*[contains(@id,'em')]").clear()
#         # driver.find_element(By.XPATH, "//*[start-with(@id,'em')]").send_keys("abc") #start-with used
#         # driver.find_element(By.XPATH, "//*[start-with(@id,'em')]").clear()
#         # driver.find_element(By.XPATH,"//*[text()='Log in']").click()
#
#
#
#
#
#
# obj=X1()
# obj.xp1()
#
