# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("try"))
#
"""qdhtfygkj"""
# w,m=1,2
# print(w)
# m,w=w,m
# print(w)

#arithmetic operators
# s=3
# v=9
# print(s*v) #27
# print(s+v) #12
# print(s-v)#-6
# print(s/v) #0.3
# print(s//v) # 0
# print(s%v) # 3
# print(s**v) #
#print(sv)
#Relational /comparision
# s=3
# v=6
# print(s<v) #T
# print(s>v) #F
# print(s>=v) #F
# print(s<=v) #T
# print(s!=v) #T
# print(s==v) #F

"""Logical operators"""
# x,y=2,3
# print(x<y and x!=y)
# print(x>y or x<=y)
# print(not(x>y or x<=y))
# print(1+2)
# print(1.5+5)
# print("ihub"+"ijioj")
# try:
#     print("oj"+8)
# except Exception as e:
#     print(e)
# try:
#     print(7.8+"ji")
# except Exception as e:
#     print(e)

#print(True+4)
# print("Name is:{} age is:{} Crores:{}".format("Raveendra Sampathi",26,1200000000))
# #print("Name is :{} Age is {} Company is:{}".format("Raveendra Sampathi",28,"SSSSolutions"))
# Sal=input("Enter the value:")
# sal1=input("Enter the value:")
# print(int(Sal)+int(sal1))
# i=123
# f=3.8
# s="str"
# print(type(i))
# r=str(i)
# print(type(r))
# print(type(f))
# r1=int(f)
# print(type(r1))
# print(type(s))
# try:
#     t=int(s)
#     print(type(t))
# except Exception as e:
#     print(e)
"""Control statements"""
#conditional statements -[if,elif,else]
#looping statements-[for, while]
#Jumping stataments -[ break,continue]
# age=int(input("enter the age:"))
# if age>=18:
#     print("eli for vote")
# else:
#     print("not eli for vote")

# age=15
# if age>=18:
#     print("eli")
# else:
#     print("not eli")

# if True:
#     print("okay")
# else:
#     print("noo")

# if False:
#     print(" not okay")
# else:
#     print("okay")

# if 0:
#     print("okay")
# else:
#     print("not")

# number=int(input("enter the value:"))
# if number%2==0:
#     print("even")
# else:
#     print("odd")
# year=int(input("enter the year:"))
# if year%2==0:
#     print("leaf:",366)
# else:
#     print(" not leaf:",365)
# week=int(input("enter the week:"))
# if week==1:
#     print("mon")
# elif week ==2:
#     print("tue")
# elif week ==3:
#     print("wen")
# elif week ==4:
#     print("thi")
# elif week ==5:
#     print("fri")
# elif week ==6:
#     print("sat")
# elif week==7:
#     print("sun")
# else:
#     print("other")
# num=int(input("enter the values:"))
# if num>0:
#     print("positive")
# else:
#     print("negative")
# x=int(input("enter the values:"))
# y=int(input("enter the values:"))
# if x>y:
#     print("x is greater and value of x:",x)
# else:
#     print("y is greater and value of y:",y)
# x=int(input("enter the values:"))
# y=int(input("enter the values:"))
# z=int(input("enter the values:"))
# if x>y and x>z:
#     print("x is greater and x value:",x)
# elif y>x and y>z:
#     print("y is greater and y value is:",y)
# elif z>x and z>y:
#     print("z is greater and z value is:",z)
# else:
#     print("no value")
"""Range function"""
# print(list(range(1,11)))
# print(list(range(-10,0)))
# print(list(range(-10,11)))
# for i in range(1,21,2):
#     print(i)
# for i in range(0,21,2):
#     print(i*2)
# print(list(range(1,11,2)))
# print(list(range(0,11,2)))
#print(list(range(-10,0,3)))
# i=1
# while i<11:
#     print(i)
#     i+=1
# i=10
# while i>0:
#     print(i)
#     i-=1
# i=10
# if i!=3 :
#     print("yes")
# for i in range(-10,0,2):
#     print(i)
# i=10
# while i>1:
#     print(i)
#     i-=1
#     if i==5:
#         break
# for i in range(1,11,2):
#     if i==3:
#         continue
#     print(i)

# i=1
# while i<10:
#     i+=1
#     if i==3:
#         continue
#     print(i)
# for i in range(0,11,2):
#     if i==4:
#         continue
#     print(i)
# i=10
# while i>1:
#     i+=1
#     if i==4:
#         break
#     print(i)

# i=10
# while i>1:
#     print(i)
#     i-=1
#     if i==4:
# #         continue
# for i in range(1,11):
#     if i==3:
#         continue
#     print(i)
# i=1
# while i<10:
#     i+=1
#     if i==3:
#         continue
#     print(i)
# y=10
# while y>1:
#     y-=1
#     if y==6:
#         continue
#     print(y)
# s="Raveendra"
# sum=""
# for i in s:
#     sum=i+sum
#     print(sum)

# number=[1,2,3,4,5]
# sum=0
# for i in number:
#     sum=i+sum
#     print(sum)
"""Bulit-in functions"""
"""max & min"""
# s=[2,4,5]
# print(max(s))
# print(min(s))
# i=10
# while i>1:
#     i-=1
#     if i==3:
#         continue
#     print(i)
# for i in range(1,11):
#     if i==8:
#         continue
#     print(i)
#strings
# s="Raveendra"
# print(s.upper())
# print(s.lower())
# print(s.split("e"))
# print(s.split())
# print(s.split())
# print(s.count("e"))
# print(s.startswith("R"))
# print(s.endswith("a"))
# print(s[::-1])
# print(s.replace("e","E"))
# print(s.startswith("R"))
s="Raveendra"
# print(s.startswith("R"))
# print(s.strip())
# print(s.split("e"))
# print(s.replace("e","E"))
# print(s[::2])
# print(s[:5])
# print(s[2:-1])
# print(s[1:-1])
# print(s[1:3])
# print(s[:5])
# print(s[2:])
# print(s[1:-1])
# print(s[1:-2])
# print(ord("s"))
# print(chr(115))
# print(ord("s"))
# print(chr(115))
# A=1,2,3
# # print(type(A))
# Name="Raveendra"
# print(Name)
# print(id(Name))
# a=0101
# b=2
# c=a+b
# print(c)  #error it gives
# a=[10,20,30]
# for i in a:
#     print("is for blobk")
# else:
#     print("its else block")
# i=10
# while i>0:
#     i-=1
#     if i==3:
#         break
#     print(i)
# else:
#     print("else")
# i=1
# while i<10:
#     print(i)
#     i+=1
# else:
#     print("else")
# import sys
# print(sys.version)

#find the same object references count
# import sys
# x="Ravi"
# y=x
# print(sys.getrefcount(x))

#find the version pyhton through to code
# import sys
# print(sys.version)

#range And Xrange-its not theor in python3
# a=range(1,11)
# # print(type(a))
# s=["r","a","v"]
# print("r" in s)
# s="fysx"
# print(s.find("f"))
# print(s.count("f"))
# print(s.isalpha())

# s="Raveendra"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# print(s[::-1])
#ollections
# list=["Raveendra",3,True,4.5]
# print(type(list))
# list=["r",9,9.8,True]
# print(type(list))
# # list[0]="Raveendra"
# print(list)
# list=["Raveendra","Sam",25,"120crore",True]
# # print(list[::-1])
# # print(list[:2])
# # print(list[:3:2])
# list.append("Gova")
# print(list)
# list.extend(["tina","fina"])
# print(list)
# del list[7]
# print(list)
# list.pop(6)
# print(list)
# print(list[-1])
# print("gova" in list)
# for i in list:
#     if "gova" in list:
#         print("true")
#     else:
#         print("false")
# list=["Raveendra","Sam",25,"120crore",True]
# list.append("Gova")
# list.extend(["tina","fina"])
# print(list)
# print(len(list))
# list.insert(3,"Happy")
# print(len(list))
# list.pop(8)
# print(list)
# list.insert(8,"fina")
# print(list)
# del list[8]
# print(list)
# list1=list(list)
# print(list1)
#
# s=['Raveendra',5,True,1,0,8.9]
# for i in s:
#     print(i)
# s.append("Sam")
# s.insert(3,"happy")
# s.extend(["Hpy","Soo"])
# print(s)
# print(len(s))
# s.pop(5)
# del s[4]
# print(s)
# s1=[3]
# s1.clear()
# del s1
# # print(s1)
# s2=list(s)
# print(s)
# print(s2)
# s1=s
# print(s1)
# s1=s.copy()
# print(s1)
# print(s+s1)
t1=("raveendr",9,9.8)
# print(t1[::-1])
# print(t1[0:2])
# t2=list(t1)
# print(type(t1))
# print(type(t2))
# t2.pop(1)
# print(t2)
# t1=tuple(t2)
# print(type(t1))
# t2=list(t1)
# print(type(t2))
# t1=tuple(t2)
# print(type(t1))
t2=t1



