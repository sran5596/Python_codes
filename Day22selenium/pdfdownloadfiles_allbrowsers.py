from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
place=os.getcwd()#it give the current locatrion of dictionary

#below code function for the normal download
def chrome():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    opt=webdriver.ChromeOptions() #its for handle the browser pop ups
    opt.add_argument("--disable-notofications") # thios also
    driver=webdriver.Chrome(service=obj)
    return driver

#its for the desired location code
def chrome2():
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers\chromedriver.exe")
    preferences = {"download.default_directory": place,"plugins.always_open_pdf_externally":True} # it give the import os function current directory location
    #above code for the pdf
    preferences={"download.default_directory":"paste the you need location here","plugins.always_open_pdf_externally":True} #here give location
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(service=obj,options=opt)
    return driver

#its for the edge
def edge():
    from selenium.webdriver.edge.service import Service
    obj=Service("D:\drivers\msedgedriver.exe")
    preferences = {"download.default_directory": place,"plugins.always_open_pdf_externally":True} # it give the import os function current directory location
    #above for the code pdf downlad
    preferences={"download.default_directory":"paste the you need location here"} #here give location
    opt=webdriver.EdgeOptions()
    opt.add_experimental_option("prefs",preferences)
    driver=webdriver.Edge(service=obj,options=opt)
    return driver
#its for the firefox -- mime type is important
def fire_fox():
    from selenium.webdriver.firefox.service import Service
    obj = Service("D:\drivers\msedgedriver.exe")
    preferences = {"download.default_directory": place}  # it give the import os function current directory location
    preferences = {"download.default_directory": "paste the you need location here"}  # here give location
    opt = webdriver.FirefoxOptions()
    opt.set_preference("brwser.helperApps.neverAsk.saveToDisk","application/pdf") #application/pdf is mime type
    opt.set_preference("browser.download.manager.showWhenString",False) # it ignore the popup
    opt.set_preference("browser.download.folderlist",0)
    #0= downloiad on the desktop
    #1= download the download folder
    #2= downlaod the need location
    opt.set_preference("browser.download.dir",place)
    opt.set_preference("pdfjs.disabled",True)
    driver = webdriver.Firefox(service=obj, options=opt)
    return driver

driver=edge()
driver.maximize_window()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
ele=driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]")
driver.execute_script("arguments[0].scrollBy();",ele)
ele.click()
time.sleep(5)
