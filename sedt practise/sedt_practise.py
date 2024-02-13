#keyword prints below code
# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("no"))

#id values is same it have the same data
# s=100
# n=100
# print(id(s))140723538423688
# print(id(n))140723538423848

#type identify
# s="rave"
# g=12
# print(type(g)) # <class 'int'>
#print(type(s)) #<class 'str'>

#variable declear and print formatting
# a,b,c="raveendra","ravikumar","hero"
# print("a is:{} b is:{} c is:{}".format(a,b,c))
# print("{} {} {}".format("raveendra",3,"manchi maniusi"))

# exchange the values
# s=10
# n="rav"
# print(type(s)) # inr
# print(type(n)) # str
# s,n=n,s # values exchange this line
# print(type(s)) # str
# print(type(n)) # int

# define variable and deleted it
# s="ra"
# print(s)
# del s
# print(s)

#arithmetic operstors
# 1)addition(+)
# 2)substraction(-)
# 3)multi(*)
# 4)division(/)
# 5)division operator(//)
# 6)modulo division(%)
# 7)Exponentrial(**)

# a=10
# b=5
# c=3
# print(a+b)#15
# print(a-b)#5
# print(a*b)#50
# print(a/c)#3.3
# print(a//c)#3
# print(a**b)#100000
# print(a%b)#0

# odd numbers print
# for i in range(1,21,2):
# #     print(i)

# even numbers print
# for i in range(2,21,2):
#     print(i)

# print 2 mulities only
# for i in range(1,11):
#     print(i*2)

#File read and write code
# with open('D:\pythonprograms\Udemy\text.txt') as reader:
#     con=reader.readlines()
#     reversed(con)
#     with open('D:\pythonprograms\Udemy\text.txt','w') as writer:
#         for line in reversed(con):
#             writer.write(line)

# for i in range(1,11  ):
#     if i%2==0:
#         print("even is :",i)
#     else:
#         print("odd is :",i)

#comparison operators # its gives Ture or False
# a=10
# b=12
# c=7
# if a==b and b==c:
#     print("okay1")
# elif a!=b and b!=c:
#     print("okay2")
# elif a>=b and a>=c:
#     print("okay3")
# elif b>=a and b>=c:
#     print("okay4")
# elif c>=a and c>=b:
#     print("okay5")
# else:
#     print("done")

# a,b,c=2,3,1
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print(" c is greater")
# else:
#     print("no")
# print("done")

# i=int(input("enetr the value:"))
# if i>=18:
#     print("eli")
# else:
#     print("not eli")

 #concatination
# s="raveendra"
# r="sampathi"
# print(s+ r)

# r=123
# d="tina"
# print(r+d)
# d=123
# d1=456
# print(d+d1)
# d=1
# f=True
# print(d+f)

# formatting the output
# name="raveendra"
# age=25
# company="samsolutions"
# print("name is:{} age is:{} company is:{} ".format(name,age,company))

# print("name is :{} age is:{} tournover is:{}".format("sampathi raveendra",24,"500 crores"))

#input takes from user
# u=input("enter the number:")
# u1=input("enter the number:")
# print(u+u1)
# #input always consider the data is string
# print(int(u)+int(u1))

#type conversion
# r1=2
# print(type(r1))
# r2=float(r1) # it works int to float works
# print(type(r2))

# r1="raveendra"
# print(type(r1))
# r3=int(r1) # its not work string to int not work
# print(r3)

# r1=23
# print(type(r1))
# r2=str(r1) #its work int to str its okay
# print(type(r2))

#conditional statements
# if
# elif
# else

# i=int(input("enter the values:" ))
# if i>=18:
#     print("eli")
# else:
#     print("not eli")

# if True:
#     print("goo")
# else:
#     print("not")

# if False:
#     print("noo")
# else:
#     print("good")

# if 1:
#     print("okay")
# else:
#     print("not")

# if 0:
#     print("good")
# else:
#     print("goo")

# #it gives the alphabet number
# print(ord('a'))
# print(chr(97))

# i=int(input("enter the values:")) # find even or odd
# if i%2==0:
#     print("evev is:",i)
# else:
#     print("odd is :",i)

#ternary operator
# i=int(input("enter the value:"))
# print("goo") if i%2==0 else print("noo")

# i=10
# {print("good"),print("one")} if i>=20 else {print("bad"),print("one")}

# i=10
# if i>=20:
#     print("good")
#     print("one")
# else:
#     print("bad")
#     print("one")

# day=int(input("Enter the dayname:"))
# if day==1:
#     print("mon")
# elif day==2:
#     print("tue")
# elif day==3:
#     print("wed")
# elif day==4:
#     print("thi" )
# elif day==5:
#     print("fri")
# elif day==6:
#     print("sat")
# elif day==7:
#     print("sun")
# print("done")

# data=int(input("value:"))
# if data>0:
#     print("positive number:",data)
# else:
#     print("negative number:",data)

#range function
# print(range(10))
# print(list(range(11 )))
# print(tuple(range(11)))

#looping statements
# for i in range(1,11):
#     print(i)

# #evev numbers
# for i in range(0,11,2):
#     print(i)
# #odd numbers
# for i in range(0,11,2):
    #print(i)

#print minus vallues
# print(list(range(-10,0)))

#looping statements
# s="raveendra"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#While
#Rules-1)initilize 2)increase or decrese 3)condition
# r=10
# while r>=1:
#     print(r)
#     r-=1

# r=1
# while r<=10:
#     print(r)
#     r+=1

# r=int(input("enter the data:" ))
# while r%2==0:
#     print("r is even")
#     r<=10

#foor loop
# for i in range(1,11):
#     print(i)
#
# r=1
# while r<=10:
#     print(r)
#     r+=1

# for i in range(-10,0):
#     print(i)

# r=-10
# while r<0:
#     print(r)
#     r+=1

# for i in range(5,50,5):
#     print(i)

#jumpping statements
#break
#continue
# for i in range(1,10):
#     if i==6:
#         break
#     print(i)
# print("done")

# for i in range(1,10):
#     if i==6:
#         continue
#     print(i)
# print("done")

# for i in range(1,10,2):
#     if i==5:
#         break
#     print(i)
# print("done")

# for i in range(1,11,2):
#     if i==5:
#         continue
#     print(i)

#string things
#string is immutable
# s="udemy_py_se_pra"
# s[0]="j"
# print(s)

#canctination
# s="sampathi "
# r="raveendra"
# print(s+r)

#multiply of string
# s="sampathi"
# print(s*2)

#slicing the string
# s="sampathi"
# print(s[1:3])
# print(s[:5])
# print(s[2:])
#print(s[-3:-1])
#print(s[3:-3])
#print(s[::-1])
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# print(ord("a"))
# print(chr(97))

# print(max(2,5,6))
# print(min(3,5,6))
# print(len(s))

#membership opertors
#in and not in
# s="fiyaegofli"
# # print("k" in s)
# # print("i" in s)
# print("g" not in s)
# print("h" not in s)

#comparision strings
# print("raveendra"=="sampathi")
# print("raveendra"!="sampathi")
# print("raveendra">"sampathi")
# print("raveendra"<"sampathi")
# print("raveendra">="sampathi")
# print("tree"<"tr")

# s="raveendra"
# print(s.isalnum())
# print(s.isdigit())
# print(s.isidentifier())
# print(s.islower())
# print(s.isupper())
# print(s.isalpha())
# r=" "
# print(r.isspace())

# print(s.endswith("ra"))
# print(s.startswith("ra"))
# print(s.find("e"))
# print(s.count("r"))
# print(s.find("g"))
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.replace("ra","re"))

#reverse string
# print(s[::-1])
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#lists
#s=["samaphti",1,2000000,"raveendra"]
# print(s[0])
# s1=[]
# print(s1)
# print(s[1:3])
# s.append(["tina"])
# print(s)
# print(s.insert(0,"ravee"))
# print(s)
# print(s.extend(["ganga","devi"]))
# print(s)

# for i in s:
#     print(i)
#
# print(s[::-1])
# print("ravee" in s)
# print(len(s))

# del s[1]
# print(s)
# s.append("tina")
# print(len(s))
# print(s)
# s.pop(4)
# print(s)
# s1=["tova","hhhh"]
# s1.clear()
# print(s1)

#cpy the lists
#copy method

# s=[1,True,8.9,"yuva"]
# s1=s
# print(s1)
# print(id(s))
# print(id(s1))
# print(type(s1))

# s1=s.copy()
# print(s1)

# s1=["vinod"]
# print(s+s1)

# for i in s1:
#     s.append(i)
# print(s)

# for i in s:
#     s1.append(i)
# print(s1)

#creating the tuple
# t1=("tina",True)
# t2=("giva")
# t3=(3,4,5)
# # print(t1+t2)
# print(t1[0])
# print(len(t1))
# print(t1[::-1])
# print(t1[-1])
# del t1[0]

# t1=["gfdhd"]
# t2=tuple(t1)
# print(type(t2))
# l1=list(t1)
# print(type(l1))
# l1.append(["raja","rana"])
# print(l1)
#convert
# t1=tuple(l1)
# # print(t1)
# # print(type(t1))
# del l1[2]
# print(l1)
# for i in t1:
#     print(i )
# for i in t1:
#     if i=="rana":
#         print("okay")
#     else:
#         print("not")

# print(t2)
# del t2
# print(t2)

# t=("giva")
# p=t+t1
# print(p)

# t1=("a","b")
# t2=(1,2)
# t3=t1+t2
# print(t3)
# t4=("raveendra")
# #print(t1+t4)
# print(t2+t4)

# tu1=("s","a","i")
# tu2=("raveendra")
# print(tu1+tu2)
# tu3=(1,2)
# tu4=(3,4)
# print(tu3+tu4)
# print(tu3+tu1)

# # t1=("a","b","c")
# t2=(1,2,3)
# t3=("ravi","ndra")
# print(t3+t2)
# y1=("raveendra","sampathi")
# print(y1+t2)
# t1=("ton")
# print(t1*2)








