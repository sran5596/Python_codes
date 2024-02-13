import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("D:\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.maximize_window
driver.get("https://www.amazon.in/b/?ie=UTF8&node=1355016031&ext=6766-31174&ref=pd_sl_7hz2t19t5c_e&tag=googhydrabk1-21&hvpos=&hvnetw=g&hvrand=14416795191490767039&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299135&hvtargid=kwd-10573980&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458706470&hvpos=&hvnetw=g&hvrand=14416795191490767039&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299135&hvtargid=kwd-10573980&hydadcr=14453_2154373")
driver.find_element(By.XPATH("(//input[@id='twotabsearchtextbox'])[1]").send_keys("mobiles"))
driver.find_element(By.XPATH("//input[@id='nav-search-submit-button']")).click()
print(driver.title)
print(driver.current_url)
driver.back()
driver.quit()