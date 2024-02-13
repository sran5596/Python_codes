# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("NO"))
# x=19
# print(type(x))
# # y="twjfyh"
# # # print(x)
# # del y
# # print(y)
# print("age is:{} salary is:{}".format(25,"1200000"))
# r=input("value:",)
# print(type(r))
#condtional statements
# If:
# elif
# else:
# t=15
# if t>=18:
#     print("okay")
# else:
#     print("not okay")
# i=int(input("value:"))
# if i>=18:
#     print("eli")
# else:
#     print("not okay")
# i=int(input("value:"))
# if i%2==0:
#     print("even")
# else:
#     print("odd")
# i=int(input("value:"))
# if i==1:
#     print("mon")
# elif i==2:
#     print("thu")
# elif i==3:
#     print("wen")
# elif i==4:
#     print("thi")
# elif i==5:
#     print("fri")
# elif i==6:
#     print("sat")
# elif i==7:
#     print("sun")
# else:
#     print("NO")
# i=int(input("value:"))
# if 0<i:
#     print("pos")
# elif 0>i:
#     print("neg")
# a=int(input("value:"))
# b=int(input("value:"))
# # if a>b :
#     print("a value is:",a)
# elif a<b:
#     print("b value is:",b)
# else:
#     print("done")

# a=int(input("value:"))
# b=int(input("value:"))
# c=int(input("value:"))
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")

# print(range(1,10))
# print(list(range(1,19)))
# print(list(range(0,11,2)))
# # print(list(range(1,11,2)))
# print(list(range(10,0,-1)))
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# print("Done!")
# i=10
# while i>=1:
#     print(i)
#     i-=1
# for i in range(1,11):
#     print(i)
# for i in range(10,1,-1):
#     print(i)

# for i in range(1,10,2):
#     print(i)
# for i in range(0,10):
#     if i==6   :
#         break
#     print(i)

# for i in range(10,1,-1):
#     if i==5:
#         break
#     print(i)

# for i in range(10,1,-1):
#     if i==3 or i==6 or i==9:
#         continue
#     print(i)
# s="ytedfwyjh.teufdwyg"
# print(s.split("."))
# r="     yty     "
# print(r.strip())
# print(r.lstrip())
#
# s="ydqhwymsuhj"
# print(s[1:4])
# print(s[::-1])
# print(s[1:6])
# print(s[1:-1])
# # print(chr("g"))
# print(ord("v"))
# print("y" in s)
# print(s.isalpha())
# print(s.isalnum())
# y=""
# for i in s:
#     y=i+y
# print(y)
# li=["tywf",242,True,9.8]
# # print(li[0:2])
# li[2]="tye"
# print(li)
# # for i in li:
# #     print(i)
# # print(242 in li)
# # print(len(li))
# # for i in ("tyf",53674,6):
# #     print(i)
# set1={"ewgtfhx",6534,9.8,True}
# set2={"dwthfgh",8787,False,"hfg"}
# # print(type(set1))
# # print(9.8 in set1)
# # set1.add("tina")
# # print(set1)
# # set1.update([87,"eewfdh",9])
# # print(set1)
# set1.remove(True)
# print(set1)
# # set1.remove("dyeghj")
# # set1.discard("wdhgfh")
# # print(set1)
# # set3=set1.union(set2)
# # print(set3)
# set1.update(set2)
# print(set1)
#
# d1={"name":"raveendra","age":25}
# # print(d1['age'])
# for i in d1:
#     print(i)
# for i in d1:
#     print(d1[i])
# for t,n in d1.items():
#     print(t,n)
# set1={"name":"raveendra","age":25}
# for i in set1:
#     print(i)
# for i in set1:
#     print(set1[i])
# for t,n in set1.items():
#     print(t,n)
# sum=0
# for i in range(0,6):
#     sum=i+sum
#     print(sum)
#function
# def ravi(a,b):
#     print(a+b)
# ravi(2,3)

# def cal(a,b,c):
#     print(a+b*c)
# cal(4,7,8)
# def tina(name):
#     print("name is:",name)
# tina("raveendra")
# def add(a,d):
#     return a+d
# print(add(3,7))
# def name(a,b):
#     return a+b
# name()
# def t1():
#     return
# print(t1())
# def cal(a,b):
#     print(a+b)
# cal(2,3)
# def d1(a,b,c):
#     if a>b and a>c:
#         return a,b
#     elif b>c and b>a:
#         return b,c
#     elif c>a and c>b:
#         return c,a
# print(d1(a=2,b=23,c=9))
# d=20
# def t1(name):
#     u=12
#     global d
#     d=30
#     print(u)
#     print(d)
# t1("g")
# print(d)

# a,b=1,2
# class y:
#     a,b=3,4
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
#     @staticmethod
#     def y1(self,v,b):
#         print(v+b)
# obj=y()
# obj.add(5,6)
# y.y1(2,3,4)
# class one:
#     num=100
#     def __init__(self,a,c):
#         self.a = a
#         self.c = c
#         print("its called first")
#     def add(self):
#         return self.a+self.c*self.num
# obj=one(2,3)
# print(obj.add())
# class ton(one):
#     num1=200
#     def __init__(self):
#         one.__init__(self,4,5)
#     def mul(self):
#         print(self.num*self.add())
#     def yoo(self):
#         print(self.c+self.num1)
# obj1=ton()
# obj1.add()
# obj1.mul()
# obj1.yoo()
# class one:
#     def add(self):
#         print("good")
# obj=one()
# class one1(one):
#     def mul(self):
#         print("second good")
# obj=one1()
# obj.add()
# obj.mul()
#
# class one:
#     def add(self):
#         print("good")
# obj=one()
# class one1(one):
#     def mul(self):
#         print("second good")
# class one2(one1):
#     def sub(self):
#         print("third")
#
# obj=one2()
# obj.add()
# obj.mul()
# obj.sub()
#
# class one:
#     def add(self):
#         print("good")
# obj=one()
# class one1(one):
#     def mul(self):
#         print("second good")
#
# class one2(one):
#     def ti(self):
#         print("goooooooo")
#
# obj1=one1()
# obj1.add()
# obj1.mul()
# obj2=one2()
# obj2.add()
# obj2.ti()
#
# class one:
#     def add(self):
#         print("good")
# obj=one()
# class one1:
#     def mul(self):
#         print("second good")
# class one2(one,one1):
#     def run(self):
#         print("herooo")
# obj=one2()
# obj2.add()
# obj2.run
#
# #overriding
# class one:
#     def m1(self):
#         print("one")
# class two(one):
#     def m1(self):
#         print("two")
#         super().m1()
# obj=two()
# obj.m1()

#overloading
# class one:
#     def one1(self,a=1,b=0,c=9):
#         print(a+b+c)
# obj=one()
# obj.one1()
# obj.one1(1)
# obj.one1(1,2)
# obj.one1(1,2,3)
# class one:
#     name="raveendra"
# class one1(one):
#     name="sampathi"
#     # print(super().name)
#
# obj=one1()
# print(obj.name)

# class one:
#     def add(self,a,d):
#         return a+d
#     def add(self,a,b,c=1):
#         return a+b+c
# obj=one()
# print(obj.add(1,2))
# print(obj.add(2,3,4))
# from Day_9.pack1 import display
# display.fun2()
# from Day_9.a import hu
# obj=hu()
# obj.fun2()
# from Udemy.text.txt import *
# with open('D:\pythonprograms\Udemy\text.txt','r') as reader:
#     print(reader.read())
# from Day_9.pack1 import display
# display.fun2()
# file=open('text.txt','r')
# for i in file.readlines():
#     print(i)

# year=int(input("enter the value:"))
# if year%2==0:
#     print("leaf year")
# else:
#     print("not leaf year")
