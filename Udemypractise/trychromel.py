try:
    class fun:
        def fun1(self):
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            obj=Service("D:\drivers\chromedriver.exe")
            driver=webdriver.Chrome(service=obj)
            driver.get("https://www.flipkart.com")
            print(driver.title)
            driver.quit()
    obj=fun()
    obj.fun1()

except Exception as e:
    print(e)
finally:
    print("done")
