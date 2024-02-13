from Udemypractise.call2 import che2


# def chrome():
#         from selenium import webdriver
#         from selenium.webdriver.chrome.service import Service
#
#         obj=Service("D:\drivers\chromedriver.exe")
#         driver=webdriver.Chrome(service=obj)
#         driver.maximize_window()
#         driver.get("https://www.flipkart.com/")
#         print(driver.title)
#
# chrome()


class child(che2):

        def fun(self,a,b):
                self.a=a
                self.b=b
                return(a+b)


obj=child()
obj.chrome()

