class che2:

    def chrome():
        from selenium import webdriver

        from selenium.webdriver.chrome.service import Service

        obj = Service("D:\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=obj)
        driver.maximize_window()
        driver.get("https://www.flipkart.com/")
        print(driver.title)
    chrome()

obj=che2()
obj.chrome()