# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("u"))
#below code for palindrome =reverse the given name its same or not
# name=input("Enter your name:")
# name1=name[::-1]
# if name==name1:
#     print("palindrome")
# else:
#     print("not palindrome")

# sum=0
# for i in range(1,6):
#     sum=sum+i
#     print(sum)
# print(sum)

# name="raveendra"
# print(name[::-1])
# list=[3,4,5,6,9]
# # largest=max(list)
# # print(largest)
# for i in list:
#     print(max(i))

#swapping
# num=int(input("Enter a number:"))
# num1=int(input("Enter a number:"))
# print("before :",num,num1)
#
# temp=num
# num=num1
# num1=temp
# print("after :",num,num1)
# print(num)
# print(num1)

#prime number
# num=int(input("Enter a number:"))
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("prime")
#     else:
#         print("not prime")
#
#factorial number
# num=int(input("Enter a number:")) #== firstone
# factorialnumber=1
# for i in range(1,num+1):
#     sum=sum*i
# print(sum)
# fact=1

# num=int(input("Enter a number:")) #second one
# if num<0:
#     print("NO FACTORIAS")
# elif num==0:
#     print("zero factorial is 1")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)

# def factorial(n): # third one
#     if n==0 or n<0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def factorial(n): # fourth one
#     #ternary operator
#     return 1 if(n==1 or n==0) else n*factorial(n-1)
# print(factorial(7))
# ravi=["e",5,"h",0,"y"]
# for i in ravi:
#     if type(i)==int:
#         print(i)
#     else:
#         print("not int:",i)
# num=int(input("Enter a number:"))
# count=0
# if num>0:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("prime:",num)
#     else:
#         print("not primenum:",num)

# name="Raveendra"
# reverse_str=""
# for i in name:
#     # reverse_str=reverse_str+i
#     # print("rev+i:",reverse_str)
#     reverse_str=i+reverse_str
# print("i+rev:",reverse_str)
# print(name[::-1])
# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)
# def factorial(n):
#     if n==0 or n<0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))
#arithmetic operators
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #float
# print(a//b) #int
# print(a%b) #remainder,0 or 1
# print(a**b) #power
# num=5
# num1=8
# print("firstone:{} secondone:{}".format(num,num1))
# try:
#     print("first:{} second:{}"
#         .format(num=int(input("Enter a number:")),
#                 num1=int(input("Enter a number:"))))
# except:
#     print("invalid input")

# age=int(input("Enter your age:")) or float(input("Enter your age:"))
# if age>18 or age==18:
#     print("eligible")
# else:
#     print("not eligible")
# for i in range(1,11):
#     if i==4:
#         # break
#         continue
#     print(i)
# for i in range(-11,0):
#     if i==-5:
#         continue
#     print(i)
# i=0
# while i<10:
#     print(i)
#     i=i+1
# i=10
# while i>0:
#     print(i)
#     i=i-1
# i=-10
# while i<0:
#     print(i)
#     i=i+1
#lambda functtion
# div=lambda a,b:a%b
# if div==0:
#     print("divisible:",div)
# print(div(4,5))
# mul=lambda a,b:a*b
# print(mul(4,5))
# madulo=lambda a,b:a%b
# print(madulo(4,2))
# for i in range(-10,0):
#     if i==-5:
#         # continue
#         break
#     print(i)
# st="uyejfguwekfgu             "
# # print(st.split("u"))
# # print(st.rstrip())
# print(st[0:4:2])
# lis=["raveendra",9,"hgiu"]
# print(lis[::-1])
# lis.append("hhh")
# print(lis)
# lis.insert(1,["igyuy"])
# print(lis)
# lis.extend(["ghgu"])
# print(lis)
# lis.append([3,"hfjf",55])
# print(lis)
# print(lis[::-1])
# print(len(lis))
# print(lis[2:5])
#
# lis[2]="gon"
# print(lis)
# for i in lis:
#     print
# print(lis.count("gon"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,10):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3
# print(n3)
# set1={"jjj",8,"l"}
# set1.add("kk")
# set1.update("jdd")
# print(set1)
# set1.update(["jin",7.9])
# print(set1)
# set2=set1.copy()
# print(set2)
# set3=set1.union(set2)
# print(set3)
# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict["key4"]="value4"
# print(dict)
# for i in dict:
#     print(i)
# for i in dict:
#     print(dict[i])
# for i in dict.values():
#     print(i)
# for i,j in dict.items():
#     print(i,j)
# for i,j in dict.items():
#     print(i,j)
# print(dict["key1"])
# glo=10
# def fun():
#
#     global x
#     x=20
#     print(x)
# print(fun())
# x=10
# # def fun():
# #     x=20
# #     print(x)
# #     print(globals()["x"])
# # fun()
# def one(i,j=1):
#     return i+j
# print(one(2,3)) # positional arguments
# # print(one(2)) # keyword arguments
# # a,b=10,15
# # def com():
# #     if a>b:
# #         return a,b
# #     else:
# #         return b,a
# # print("a first a greater:",com())
# # print(type(com()))
# class one:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("herooo first")
#         print(self.name)
#     def sce(self):
#         print("good")
#     @staticmethod
#     def good():
#         print("goo")
# obj=one("raveendra",25)
# # obj.sce()
# # one.good()
# class two(one):
#     def __init__(self):
#         one.__init__(self,"raveendra",25)
#     def cal(self,a,d):
#         print(a+d)
# obj1=two()
# obj1.good()
# obj1.__init__()
#single
# class one:
#     def good(self):
#         print("good")
# class two(one):
#     def good1(self):
#         print("good1")
# obj=two()
# obj.good1()
#multilevel
# class one: #1
#     def good1(self):
#         print("goo1")
# class two(one): #2
#     def good2(self):
#         print("good2")
# class third(two): #3
#     def good3(self):
#         print("good3")
# obj=third()
# obj.good3()
# class one:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("herooo first")
#         print(self.a)
# class two(one):
#     def __init__(self):
#         one.__init__(self,10,20)
#     def cal(self,a,d):
#         print(a+d)
#         print(self.b*d)
# obj=two()
# obj.cal(10,20)

# class one:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("herooo first")
#         print(self.a)
#     def two1(self):
#         print(self.b)
# class two(one):
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d
#         one.__init__(self,10,20)
#         print("herooo second")
#
#     def done(self):
#         print("seconds")
# class third(two):
#     def __init__(self):
#         two.__init__(self,5,6)
#
# obj=third()

# class father:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("goo india")
#         print(self.a+self.b)
#     def hello1(self):
#         print("hello world")
# class fson(father):
#     def __init__(self):
#         father.__init__(self,10,20)
#         print(self.a*self.b)
#     def hello2(self):
#         print("hello india")
# class sson(father):
#     def __init__(self):
#         father.__init__(self,3,2)
#         print(self.b-self.a)
#     def hello3(self):
#         print("hello don")
# obj=father(2,6)
# obj.hello1()
#
# class a:
#     def __init__(self):
#         print("hello")
# class b:
#     def __init__(self):
#         print("world")
# class c(a,b):
#     def __init__(self):
#         a.__init__(self)
#         b.__init__(self)
#         print("hello")
# obj=c()
# obj.__init__()
#polymorphism
# method over loading
# same class
# same methods
# differnt parameters
#method over riding
# differnt classes (inheritance)
# same method
# different parameters
# class one:
#     def two(self,a,b):
#         print("good:",a+b)
#
#     def two(self,a,b,c=1):
#         print("two:",a+b+c)
# obj=one()
# obj.two(2,3)
# with open("D:/pythonprograms/Udemypractise/te.txt","r") as reader:
#     print(reader.readlines())
#
# with open("D:/pythonprograms/Udemypractise/te.txt","w","r") as writer:
#     writer.write("hello")
#     print(writer.read())
# file=open("D:/pythonprograms/Udemypractise/te.txt","r")
# print(file.readlines())
# for i in file.readlines:
#     print(i)
#l=[6,7,4,3,2,1] write the python programme for sorting the list items
# def bubbleSort(l):
#     n = len(l)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if l[j] > l[j+1]:
#                 l[j], l[j+1] = l[j+1], l[j]
#     return l
#
# l = [6,7,4,3,2,1]
# sorted_list = bubbleSort(l)
# print(sorted_list)
# def bu(l):
#     n=len(l)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
# l=[6,7,4,3,2,1]
# sorted=bu(l)
# print(sorted)
# def bubbleSort(l):
#     n = len(l)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if l[j] < l[j+1]:
#                 l[j], l[j+1] = l[j+1], l[j]
#     return l
#
# l = [6,7,4,3,2,1]
# sorted_list = bubbleSort(l)
# print(sorted_list)
# s=["one","two","three",9]
# print(s[-3:-1])
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.booking.com/")
#
# wait = WebDriverWait(driver, 20)
#
# try:
#     # wait for the date picker to appear
#     date_picker = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ui-datepicker-calendar')]")))
#
#     # find the number of rows in the date picker
#     rows = date_picker.find_elements_by_xpath(".//tr")
#
#     # iterate through each row
#     for row in rows:
#         # find the number of cells in the row
#         cells = row.find_elements_by_xpath(".//td")
#
#         # iterate through each cell
#         for cell in cells:
#             # if the cell is a valid date
#             if cell.get_attribute("class") != " ui-datepicker-week-end":
#                 # click on the date
#                 cell.click()
#
#                 # give some time for the page to react to the date change
#                 time.sleep(1)
#
#                 # go back to the date picker page
#                 driver.execute_script("window.history.go(-1)")
#
#                 # break out of the loop since we only want to select one date
#                 break
#
#         # break out of the loop since we only want to select one date
#         break
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     driver.quit()
