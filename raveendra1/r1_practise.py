# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# def chrome():
#     obj=Service("D:\drivers\chromedriver.exe")
#     driver=webdriver.Chrome(service=obj)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver
# driver=chrome()
# driver.get("https://chat.openai.com/")
# driver.title
# driver.current_url
# driver.refresh()
# driver.quit()

# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("try"))

# s=["g","u",3,4,5,"y"]
# for i in s:
#     if type(i)==int:
#         print(i)
    # else:
    #     print("not int")
# a,b=2,3
# print("a is :",a,"b is :",b)
# a,b=b,a
# print("a is :",a,"b is :",b)
# my_list = ["apple", "banana", "cherry"]
# string_to_check = "orange"  # Replace this with the string you want to check
#
# # Check if the string is in the list
# if string_to_check not in my_list:
#     # If the string is not in the list, add it to the list
#     my_list.append(string_to_check)
#     print(f"'{string_to_check}' added to the list.")
#
# # Print the updated list
# print("Updated List:", my_list)
# one=["y","u","i"]
# if "o" not in one:
#     one.append("o")
#     print("new list:",one)
# s="raveendra"
# # print(s[::-1])
# sum=""
# for i in s:
#     sum=i+sum
#     sum=sum+i
# print(sum)
# sum=0
# for i in range(1,6):
#     sum=i+sum
#     print(sum)
# print(sum)
# year=int(input("enter the days:",))
# if year%2==0:
#     print("this is leaf year:",year)
# else:
#     print("this is not leaf year:",year)

#arithmetic operaters
# a=7
# b=2
# s1=print(a+b)
# s2=print(a-b)
# s3=print(a*b)
# s4=print(a/b)
# s5=print(a//b)
# s6=print(a%b)
# s7=print(b**a)
#
# if s1==9:
#     print("yes")
# elif s2==5:
#     print("yes")
# elif s3==14:
#     print("yes")
# elif s4==3.5:
#     print("yes")
# elif s5==3:
#     print("yes")
# elif s6==1:
#     print("yes")
# elif s7==128:
#     print("yes")
# name="Raveendra"
# age=26
# property=120000000000000000
# print("name is :{} age is:{} property is :{}".format(name,age,property))
#concatination
#boolean=True==1,False==0
# print("Raveendra"+"Sampathi") #yes
# print(4+True)#yes
# print(3.8+6)#Yes
# try:
#     print("gun"+8)#not okay
# except Exception as e:
#     print(e)
# try:
#     print(7.9+"loi") #not okay
# except Exception as e:
#     print(e)
# try:
#     print("yu"+False) #notokay
# except Exception as e:
#     print(e)
# print(4.8+8.9)#okay
#input function
# name=input("Enter the name:")
# print(type(name))
# age=float(input("age of the person:"))
# if age>18:
#     print("valid and qualify the vote")
# else:
#     print("not qualify the vote")
# sal=input("enter the sal:")
# total=input("enter the total:")
# print(int(sal)+int(total))
#convartions
# a=1
# print(type(a))
# s1=str(a)
# print(type(s1))
# name="Raveendra"
# name2="Sampathi"
# try:
#     s2=int(name)
#
# except Exception as e:
#     print(e)
# try:
#     s3=float(name2)
# except Exception as e:
#     print(e)
#control statements
#conditional statements =if elif else
#looping statements =for while
#jumping statements =break continue
# age=int(input("Enter the age of the person: "))
# if age>=18:
#     print("yes and valid")
# else:
#     print("not okay and not valid")
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# c=int(input("enter the value:"))
# if a>b and a>c:
#     print("a is greater:",a)
# elif b>a and b>c:
#     print("b is greater:",b)
# elif c>a and c>b:
#     print("c is greater:",c)
# else:
#     print("gooo")
# if True:
#     print("okay")
# else:
#     print("not")
# num=float(input("enter the value:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")
# weak=int(input("enter the value:"))
# if weak==1:
#     print("mon")
# elif weak==2:
#     print("tue")
# elif weak==3:
#     print("wed")
# elif weak==4:
#     print("thi")
# elif weak==5:
#     print("fri")
# elif weak==6:
#     print("sat")
# elif weak==7:
#     print("sun")
# num=int(input("enter the value:"))
# if num>0 :
#     print("positive")
# elif num==0:
#     print("zero not positive and not negative")
# else:
#     print("negative")
# num=int(input("enter the value:"))
# num1=int(input("enter the value:"))
# if num>num1:
#     print("num is greater")
# elif num1>num:
#     print("num1 is greater")
# num=int(input("enter the value:"))
# num1=int(input("enter the value:"))
# num3=int(input("enter the value:"))
# if num>num1 and num>num3:
#     print("num is greater:",num)
# elif num1>num and num1>num3:
#     print("num2 is greater:",num1)
# elif num3>num and num3>num1:
#     print("num3 is greater:",num3)
# else:
#     print("not greater")
# weak=input("enter the value:")
# if weak=="wed":
#     print("3")
# elif weak=="sun":
#     print("7")
# elif weak=="fri":
#     print("5")
# elif weak=="mon":
#     print("1")
# elif weak=="tue":
#     print("2")
# elif weak=="sat":
#     print("6")
# elif weak=="thi":
#     print("4")
#range fundtion
#
# print(list(range(0,11)))
# # print(list(range(0,11,2)))
# # list1=list(range(1,11))
# # for i in list1:
# #     print(i*4)
# print(list(range(-11,0)))
# print(list(range(1,11,2)))
# print(list(range(-20,0,2)))
#print(list(range(10,0,-1)))
#Looping statements
# i=0
# while i<10:
#     i+=1
#     print(i)
# i=11
# while i>1:
#     i-=1
#     print(i)
# for i in range(1,11):
#     print(i)
# for i in range(-11,0):
#     print(i)
# for i in range(0,11):
#     print(i*2)
# i=0
# while i<10:
#     i+=1
#     print(i*2)
# for i in range(-20,0,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
# for i in range(0,100,5):
#     print(i)
#Breaking statments
#break
#continue
# i=0
# while i<10:
#     i+=1
#     print(i)
#     if i==5:
#         break
# i=-11
# while i<0:
#     i+=1
#     print(i)
#     if i==-5:
#         break
# i=1
# while i<10:
#     i+=1
#     print(i)
#     if i==6:
#         continue

# for i in range(1,11):
#     if i==5 or i ==6 or i==3:
#         continue
#     print(i)
# i=0
# while i<10:
#     i+=1
#     if i==6:
#         continue
#     print(i)
# i=-10
# while i<0:
#     i+=1
#     if i==-2:
#         continue
#     print(i)
# for i in range(-10,0,2):
#     if i==-2:
#         continue
#     print(i)
# s="ram"
# print(id(s))
# s1=s+"sam"
# print(id(s1))
# try:
#     if id(s)==id(s1):
#         print("okay")
#     else:
#         print("nooooo")
#     assert id(s)==id(s1)
# except Exception as e:
#     print(e)
# s="ravi"
# print(s+"Sam")
# print(s*2)
# name="Sampathi Raveendra"
# print(name[::-1])
# newname=""
# for i in name:
#     newname=i+newname
#     print(newname)
# print(newname)
# i=10
# while i>0:
#     i-=1
#     if i==2 or i==5:
#         continue
#     print(i)
# for i in range(1,11,2):
#     if i==3 or i==5:
#         continue
#     print(i)
# name="Samapthi765Raveendra"
# s=["j",87,98,"p"]
# print(name[0:4])
# print(name[-5:-1])
# for i in s:
#     if type(i)==int:
#         print(i)
# name="SampathiRaveendra"
# print(name[::-1])
# print(name[2:9])
# print(name[:5])
# print(name[-5:0])
# print(name[5:])
# print(name[2:-1])
# print(name[1:-5])
# print(ord("a"))
# print(chr(97))
# for i in range(1,11):
#     if i==3 or i==4:
#         break
#         continue
#     print(i)
# i=0
# while i<=10:
#     i+=1
#     if i==4:
#         continue
#     print(i)
#
# print(ord("a"))
# print(chr(67))
# name="SampathiRaveendra"
# sum=""
# for i in name:
#     sum=i+sum
# print(sum)
# print(max(name))
# print(min(name))
# print(id(name))
# print(len(name))
from operator import concat
# s=["Raveendra",768,"lko"]
# if "w" not in s:
#     s.append("w")
#     print(s)
# print("pooiuig">="qqweiedj")
name="   Sampathi   "
# print(name.isalpha())
# print(name.isalnum())
# print(name.isdigit())
# print(name.isspace())
# print(name.isidentifier())
# print("try".isidentifier())
# print(name.startswith("S"))
# print(name.endswith("T"))
# print(name.split("a"))
# print(name.strip(    ))
# print(name.lstrip())
# print(name.rstrip())
# print(name.count("a"))
# print(name.find("a"))
# s="tinatimna"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.swapcase())
# print(s.replace("t","O"))
#python Collections-list,tuple,set,dict
#list
# s1=["Raveendra",987,"uyt","wefyu",8087,"tdufdhkj"]
# print(s1[0:2])
# print(s1[::-1])
# print(len(s1))
# print(s1[:3])
# print(s1[-1])
# s1[5]="hero"
# print(s1)
# for i in s1:
#     print(i)
# print(s1.count(987))
# if "Raveendra" in s1:
#     s1.append("Raveendra")
#     print(s1)
# s1=["Raveendra",987,"uyt","wefyu",8087,"tdufdhkj"]
# print(s1[:5:2])
# for i in range(1,11,2):
#     print(i)
# print(len(s1))
# s1[5]="hero"
# print(s1)
# s1.append(["somu","kareem"])
# print(s1)
# s1.append(909)
# print(s1)
# print(type(s1))
# print(s1)
# s2=['Raveendra', 987, 'uyt', 'wefyu', 8087, 'hero', ['somu', 'kareem'], 909]
# print(len(s2))
# s2.insert(9,"don")
# print(s2)
# print(s2.pop(8))
# del s2[7]
# print(s2)
# s3=["uygf",9870,"iu"]
# print(len(s3))
# s3.clear()
# print(len(s3))
# s1=["+","-",")"]
# print(s1+s2)
# s0=s1
# print(s0)
# if s1==s2:
#     print("equal")
# else:
#     print("not")
# s=['Raveendra', 987, 'uyt', 'wefyu', 8087, 'hero', ['somu', 'kareem'], 909]
# s1=["+","-",")"]
# for i in s:
#     s1.append(i)
# print(s1)
# t1=("ytdfych",876889,"dutwv")
# s1=list(t1)
# print(type(t1))
# print(type(s1))
# s1.append("herooo")
# print(s1)
# t1=tuple(s1)
# print(t1)
# for i in t1:
#     # print(t1)
# s=("h",6,"o",9)
# t=list(s)
# print(type(t))
# t.append("U")
# print(t)
# s=tuple(t)
# print(type(s))
# for i in s:
#     print(i)
# if "u" in s:
#     print("okay")
# else:
#     print("not in")
# t1=("o")
# # del t1
# print(t1)
# t=("p","o")
# t1=("i",98)
# t2=t+t1
# print(t2)
#set
# s1={"r","a",True,9.09,8}
# for i in s1:
#     print(i)
# if "a" in s1:
#     print("yes")
# else:
#     print("no")
# s1.add("Good")
# print(s1)
# s1.update(["good","hero"])
# print(s1)
# s1.remove("hero")
# print(s1)
# try:
#     s1.remove("k")
# except Exception as e:
#     print(e)
# s1.remove("k")
# s1.discard("k")
# s1={"k"}
# s2={"h"}
# s3=s1.union(s2)
# print(s3)
# t1=("l")
# del t1
# try:
#     print(t1)
# except Exception as e:
#     print(e)
# s1={"hero"}
# s2={"Raveendra"}
# s3=s1.union(s2)
# print(s3)
# s1.update(s2)
# print(s1)
# s1.clear()
# print(s1)
#dict
# dc={"name":" sampathi Raveendra","age":26,"salary":400000000000000}
# print(dc.get("salary"))
# print(dc["name"])
# print(dc["age"])
# print(dc.get("age"))
# dc["name"]="sampathi Raveendra"
# print(dc)
# for i ,j in dc.items():
#     print(i,j)
#     # print("/n")
# for i in dc:
#     print(i)
#     # print("/n")
# for j in dc:
#     print(dc[j])
#     # print("/n")
# for j in dc.values():
#     print(j)
#     # print("/n")
# for i,j in dc.items():
#     print(j,i)
# dc={"name":" sampathi Raveendra","age":26,"salary":400000000000000}
# # dc["total money"]=12000000000000000000000
# # print(dc)
# # dc.pop("total money")
# # print(dc)
# for i ,j in dc.items():
#     print(j,i)
#functions
# def one():
#     print("hero")
# one()
# def calculater(a,b):
#     return(a+b)
# print(calculater(2,3))
# def call(name):
#     print("udemy_py_se_pra"+name)
# call("Raveendra")
# #variables
# global_var=20
# def one():
#     local_car=10
#     print(local_car)
#     print(global_var)
# one()
# print(global_var)
# def on1():
#     global x
#     x=100
#     print(x)
# on1()
# print(x)
# x=100
# def hero():
#
#     global x
#     x=200
#     print(x)
# hero()
# print(x)
# s=100
# def heroo():
#     global v
#     v=200
#     print("onee")
# heroo()
# print(v)
# print(s)
# s=12
# def good():
#     global s
#     s=200
#     print(s)
# good()
# print(s)
#arguments
#positional,keyword
# def one(i,j):
#     print(i+j)
# one(2,3)
# def one(u,z):
#     return u+z
# print(one(2,0))
# def nee(d,f=9):
#     print(d+f)
# nee(3)
# def one(a,b,c=7):
#     if a>b and a>c:
#         print(a,b)
#     elif b>a and b>c:
#         print(b,a)
#     elif c>a and c>b:
#         print(c,a)
# one(2,3,8)
# def herooo(a,b,c):
#     print(a+b+c)
# herooo(c=8,a=9,b=9)
#OOPs
#classs and object
# one=10
# class calculater:
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("its first")
#
#     def add(self):
#         return self.a*one
#         print(self.b+self.a)
#
#     def sub(self):
#         c=100
#         return (self.a+one+c)
# obj=calculater(3,4)
# print(obj.add())
# print(obj.sub())
# class sam:
#
#     def heroo(self):
#         pass
#
#     def one(self,a,b):
#         print(a+b)
# obj=sam()
# obj.heroo()
# obj.one(3,5)
#instance methods=call only with object
#static method=call with help of call also
# class calculater:
#     global h
#     h=300
#     one=100
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("first its")
#
#     def herooo(self):
#         c=100
#         print(self.a+self.b+c+self.one)
#
#     @staticmethod
#     def static(self,num):
#         print(num+calculater.one+h)
#
# obj=calculater(2,3)
# obj.herooo()
# calculater.static(5,9)
#variables
#global
#class
#local
# r=100
# class one:
#     d=9
#
#     def good(self,i,u):
#         print(i+u)
#         print(u+one.d)
#         print(one.d+r*i)
# obj=one()
# obj.good(4,5)
# print(r)
# print(one.d)
# a,b=1,2
# class car:
#     a,b=4,5
#
#     def one(self,a,b):
#         print(a,b) # local
#         print(self.a,self.b)
#         print(car.a,car.b)
#         print(globals()['a'],globals()['b'])
# obj=car()
# obj.one(3,4)
# class emp:
#
#     def __init__(self,eid,name,sal):
#         self.eid=eid
#         self.name=name
#         self.sal=sal
#         print("its first")
#         print(self.eid)
#         print(self.name)
#         print(self.sal)
#
#     def cal(self,c):
#         print(c*self.sal)
# obj=emp(101,"Raveendra",12000000000000)
# obj.cal(4)
#inheritance
#single
#multi level
#hirarchial
#mulitple
# class one:
#
#     def one(self):
#         from selenium import webdriver
#         from selenium.webdriver.chrome.service import Service
#         obj=Service("D:\drivers\chromedriver.exe")
#         driver=webdriver.Chrome(service=obj)
#         driver.maximize_window()
#         driver.get("https://testcasehub.net/result.php?q=login")
#         return driver
#
# driver=one()
#
#class two(one):
#
#     def good(self):
#         print("good")
#
# tt=two()
# tt.one()
#multi level
# class one:
#     var=100
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     print("goood its first")
#
#     def best(self):
#         print("one-one")
#
#     def calu(self,b):
#         print(self.var+b)
#
# class two(one):
#
#     def __init__(self):
#         one.__init__(self,3,4)
#
#     def yyy(self):
#         print("two-one")
#
# class three(two):
#
#     def three(self):
#         print("three-one")
#
# class four(three):
#     def four(self):
#         print("four-one")
# obj=four()
# obj.calu(8)
# obj.best()
# obj.three()
# obj.yyy()

#hirarchail
# class one:
#
#     num=100
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     print("its hirarchial")
#
#     def one(self):
#         print("onday")
# class two(one):
#
#     def __init__(self):
#         one.__init__(self,2,3)
#
#     def its(self):
#         print("its second hirarachail")
# class three(one):
#
#     def __init__(self):
#         one.__init__(self,7,8)
#
#     def hoo(self):
#         print("its hirarachial thereee")
# obj=two()
# obj.one()
# obj1=three()
# obj1.one()

# multiple
# class a:
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def a1(self):
#         print("a-one")
#
# class b:
#
#     def __init__(self,h,j):
#         self.h=h
#         self.j=j
#
#     def b1(self):
#         print("b-one")
#
#
# class c(a,b):
#
#     def __init__(self):
#         a.__init__(self,3,8)
#         b.__init__(self,7,6)
#
#     def c1(self):
#         print("c-one")
#         print(self.h+self.a)
#         print(self.j*self.b)
# obj=c()
# obj.a1()
# obj.c1()
#Polymorphism -one thing is many forms
#overriding-diff class same methods different parameters
# class a:
#     def __init__(self):
#         print("heroo")
#
#
#     def m1(self):
#         print("one")
#
#
# class b(a):
#     def __init__(self):
#         print("goo")
#
#
#     def m1(self):
#         print("second")
#         super().m1()
# obj=b()
# obj.m1()
#overloading
# class cal:
#
#     def __int__(self):
#         print("heroo")
#
#     def m1(self,a,b):
#         return a+b
#
#     def m1(self,a,b,c=0):
#         return a+b+c
# obj=cal()
# print(obj.m1(2,3,4))
# print(obj.m1(6,8))
# class a:
#     name="Raveendra"
#
#     def m1(self):
#         print("hero")
# class b(a):
#
#     def m1(self):
#         print("good")
#         super().m1()
#         print(super().name)
# obj=b()
# obj.m1()

#Hirarchy
# class discunts:
#
#     def products(self):
#         product=int(input("enter the products count:"))
#         if product==0:
#             return 0
#
# class list(discunts):
#     def products1(self):
#         product=int(input("enter the list:" ))
#         if product>=1:
#             # return product*0.1
#             print(product-product*0.1)
#
# class list2(discunts):
#     def products2(self):
#         product=int(input("enter the list:"))
#         if product>=2:
#             print(product*0.3)
#             print(product-product*0.3)
#
# obj=list()
# # print(obj.products())
#
# obj1=list2()
# # print(obj1.products2())
# obj=list2()
# print(obj.products2())

def one(a,b):
    num=100
    print("hero")
    print(a+b+num)
def sec(j,k,l):
    print(j*k/6)

def third(u,i):
    print(u*i)













