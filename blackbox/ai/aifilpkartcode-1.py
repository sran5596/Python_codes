from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Open the Flipkart application
driver = webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.get("https://www.flipkart.com/")
# Search for mobiles
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("mobiles")
search_bar.send_keys(Keys.RETURN)
# Add three different phones to cart
phones = driver.find_elements_by_class_name("_31qSD5")
for phone in phones[:3]:
    add_to_cart_button = phone.find_element_by_class_name("_3v1-ww")
    add_to_cart_button.click()
# See the add cart page
driver.get("https://www.flipkart.com/cart")
# Print the names of the phones in the cart
for phone in driver.find_elements_by_class_name("_31qSD5"):
    print(phone.text)
# Close the browser
driver.close()
