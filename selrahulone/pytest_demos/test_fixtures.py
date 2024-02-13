from selrahulone import *
import pytest

@pytest.fixture(scope="class")
def chrome_browser(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    obj=Service("D:\drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=obj)
    driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.close()


# def test_register(chrome_browser):
#     driver.find.element(By.XPATH,"//input[@id='FirstName']").send_keys("Raveendra")
