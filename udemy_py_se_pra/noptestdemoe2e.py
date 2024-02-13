try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    Service("D:drivers/msedgedriver.exe")
    driver = webdriver.Edge()
    driver.get("https://demo.nopcommerce.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    mywait=WebDriverWait(driver,10)
    mywait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Books']")))
    driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Books']").click()
    time.sleep(5)
    items=driver.find_elements(By.XPATH,"//div[@class='product-item']")
    print(len(items))
    for product in items:
        needproduct=product.find_element(By.XPATH,"div[2]/h2").text
        if needproduct=="First Prize Pies" :
            product.find_element(By.XPATH,"div[2]/div[3]/div[2]/button[1]").click()
            time.sleep(5)
            break
    driver.find_element(By.XPATH, "//span[@class='cart-label']").click()
    time.sleep(5)
    mywait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='qty-input' and @id='itemquantity11221']"))).clear()
    # driver.find_element(By.XPATH,"//input[@class='qty-input' and @id='itemquantity11221']")
    # time.sleep(5)
    driver.find_element(By.XPATH,"//input[@class='qty-input' and @id='itemquantity11221']").send_keys("2")
    time.sleep(5)
    sub=driver.find_element(By.XPATH,"//table[@class='cart-total']/tbody/tr/td[2]/span[1]")
    total=driver.find_element(By.XPATH,"//table[@class='cart-total']/tbody/tr[4]/td[2]/span")
    time.sleep(5)

    if (sub.text)==(total.text):
            print("pass")
    else:
            print("fail")
    assert (sub.text)==(total.text),"equal and good to goo"




except Exception as e:
    print(e)