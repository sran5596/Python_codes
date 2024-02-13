def test_firstone():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    obj=Service("D:\drivers/chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    return driver
driver=test_firstone()
driver.get("https://www.flipkart.com/")
# tit=print(driver.title)
# assert "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!" in tit

