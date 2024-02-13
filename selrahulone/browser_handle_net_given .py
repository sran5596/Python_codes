import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element=By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a"
def wait_for_element(driver,element, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, element)))
        return element
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    obj=Service("D:\drivers/chromedriver.exe")
    # driver = webdriver.Chrome(service=Service("D:\drivers/chromedriver.exe"))
    driver=webdriver.Chrome(service=obj)
    driver.get("")

    # Wait for the element to load
    element = wait_for_element(driver, "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    if element:
        print("Element found!")
    else:
        print("Element not found.")

    driver.quit()

if __name__ == "__main__":
    main()