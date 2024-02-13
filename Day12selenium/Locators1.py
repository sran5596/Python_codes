#ID
#NAME
#TYPE
#LINKED_TEXT--(give the full name)
#PARTIAL_LINK_TEXT--(give the some portion of name)


class d1:
    num=10
    def __init__(self,a,s):
        self.a=a
        self.s=s
        print("its first")

    def add(self):
        return self.a+self.s+self.num


    def p1(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        obj=Service("D:\drivers\chromedriver.exe")
        driver=webdriver.Chrome(service=obj)
        driver.maximize_window()
        driver.get("https://admin-demo.nopcommerce.com/login")
        driver.find_element(By.ID,"Email").clear() # used the ID-Attribute
        driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
        driver.find_element(By.NAME,"Password").clear()
        driver.find_element(By.NAME, "Password").send_keys("admin")
        driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        print(driver.title)
        #driver.find_element(By.XPATH,"//img[@class='brand-image logo d-block d-md-none d-sm-block d-sm-none']")
        driver.find_element(By.LINK_TEXT,"Dashboard").click()
        exp_title=driver.title
        act_title="Dashboard / nopCommerce administration"
        if exp_title==act_title:
            print("website sucessfully logined")
        else:
            print("not")
        #driver.find_element(By.LINK_TEXT," Dashboard").click()
        #time.sleep(5)
        driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
        driver.back()
        #print(driver.current_url)
        #time.sleep(10)
        slides=driver.find_elements(By.TAG_NAME,"a")
        print(len(slides))
ob1=d1(2,3)
ob1.p1()
print(ob1.add())
