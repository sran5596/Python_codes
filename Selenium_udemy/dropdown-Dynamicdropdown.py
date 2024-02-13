class dr1:
    def st(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        obj=Service("D:\drivers\chromedriver.exe")
        driver=webdriver.Chrome(service=obj)
        driver.implicitly_wait(10)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        dr=Select(driver.find_element(By.XPATH,"//*[@id='dropdown-class-example']"))
        dr.select_by_index(2)
        time.sleep(5)
        dr.select_by_index(3)
        time.sleep(5)
        tag=driver.find_elements(By.TAG_NAME,"option")
        print(len(tag))
        driver.quit()
    def st1(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        obj = Service("D:\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=obj)
        driver.implicitly_wait(10)
        driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
        driver.find_element(By.XPATH,"//*[@id='autosuggest']").send_keys("ind")
        time.sleep(5)
        cou=driver.find_elements(By.CLASS_NAME,"ui-menu-item")
        print(len(cou))
        for one in cou:
            print(one.text)
            if one.text=="India":
                break
        #print(driver.find_elements(By.CLASS_NAME, "ui-menu-item").text)
        print(driver.find_elements(By.CLASS_NAME, "ui-menu-item").get_attribute("value"))
        


        driver.quit()

obj=dr1()
obj.st()
obj.st1()
