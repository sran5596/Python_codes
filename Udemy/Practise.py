# s=[33,5,56,6,"fuywge",True]
# print(s[::-1])
# print(s[2:5 ])
# s.extend(["ravi"] )
# print(s)
# s.append("ravi ")
# print(s)
# s[2]="raveendra" # its update the value
# print(s)
# s.pop(0)
# print(s)
# print(s)
# del s[0]
# print(s)

#dict
# s={"name":"raveendra",4:"raja","age":25}
# print(s[4])
# print(s.keys())
# print(s.values( ))
# s=[2,3,45,"tsf",True]
# s[1]="raveendra"
# print(s)

# dict1={} # create the empty dict and below give the keys and values to the dict
# dict1["name"]="Raveendra"
# dict1["age"]=25
# dict1["salary"]=200000
# print(dict1)

# i=1
# while i<=10:
#     print(i)
#     i+=1
# print("Done")
# i=10
# while i>=1:
#     print(i)
#     i-=1
# print("Done ")
# s="yfyiw"
# rev=""
# for i in s:
#     rev=i+rev
# print("reversed string is:",rev)
# print(s[::-1])

# for i in range(1,11,2):
#     print(i)
# for i in range(0,11,2):
#     print
# obj=[2,4,55,678,8]
# for i in obj[::-1]:
#     print(i)
# obj=[2,4,6,8,9]
# for i in obj[::-1]:
#     print(i*2)

#sum of first five natural numbers
# i=1
# r=0
# while i<=5:
#     print(r)
#     r+=i
# print("done")

# r=1
# sum=0
# while r<=5:
#     print(sum)
#     sum=sum+r
# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)

# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1 # it print-1,2,3,4

#Sum of first five natural numbers using while
# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print("ths sum is:",sum)
# sum=0
# for i in range(1,6):
#     sum=sum+i
#     print("sum of natural numbers:",sum)

# n=int(input("enter the number:"))
# i=int(input("enter the number:"))
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print("sum of the first five natural numbers:",sum)
# for i in range(10,0,-1):
#     print(i)
# print("while start")
# i=10
# while i>=1:
#     print(i)
#     i-=1

#Skipping the numbers

# i=5
# while i>=1:
#     if i!=2:
#         print(i)
#     i-=1

# for i in range(1,6):
#     if i==2:
#         continue
#     print(i)

#
# i=5
# while i>=1:
#     if i==2:
#         continue
#     print(i)
#     i-=1

# i=5
# while i>=0:
#     if i==2:
#         break
#     print(i)
#     i-=1
# for i in range(10,1,-1):
#     if i==9:
#         i=i-1
#         continue
#     if i==3:
#         break
# print(i)

#skipping the values using below continue and break statements
# it=10
# while it>=1:
#     if it==9:
#         it=it-1
#         continue
#     if it==3:
#         break
#     print(it)
#     it-=1
#
# for i in range(10,1,-1):
#     if i==9:
#         i=i-1
#         continue
#     if i==3:
#         break
#     print(i)

#function -- is group of realated statements and it perform the specific task

# Ex-1--just create the function
# def ravi():
#     print("raveendra getting the monthly 200000")
#
# ravi()

#ex-2 -- here creating the function and passing the parameters[name,age]
# def greet(name,age):
#     print("goodmrg"+name+age)
# greet("raveendra","twentyfive")

#ex-3--adding the values
# def rv():
#     print("never give up")
# def addbest(a,b):
#     print(a+b)
#
# rv()
# addbest(4,7)

#Functions examples
# def addcal(a,b):
#     return(a+b)
# def mulcal(a,b):
#     return(a*b)
# def divcal(a,b):
#     return(a/b)
# print(addcal(2,4))
# print(mulcal(4,7))
# print(divcal(3,8))

#class exmaple
# class calculator:
#     num=3
#     def addcal(self,a,b):
#         return a+b
#     def mulcal(self,c,d):
#         return c*d
#     def divcal(self,n,m):
#         return n/m
#
# obj=calculator()
# print(obj.addcal(2,4))
# print(obj.divcal(3,6))
# print(obj.mulcal(3,5))
# print(obj.num)

# class one:
#     def getone(self):
#         print("never give up one")
#     def __int__(self): # constructor
#         print("never give up two")
#     def goo(self):
#         print("nover give up three")
# obj=one()
# obj.getone()
# obj.goo()
# obj.__int__()

# code for class and parameters calling
# class calculator:
#     num=20 # class variable
#
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#         print("it first called always")
#
#     def newone(self):
#         print("never give up")
#     def sum(self):
#         return self.a + self.b + self.num
#         print("good way go never give up")
# obj = calculator()
# obj.__int__(2,3)
# obj.newone()
# print(obj.sum())

# class calculator:
#     num=20 # class variable
#
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#         print("it first called always")
#
#     def newone(self,v,n):
#         self.v=v
#         self.n=n
#         return self.v + self.num +self.n
#         print("never give up")
#     def sum(self):
#         return self.a + self.b + self.num
#         #return "good way go never give up"
# obj = calculator()
# obj.__int__(3,5)
# print(obj.newone(3,6))
# print(obj.sum())
#
# def calculator():
# #     print("calculation part")
# # def sum(a,b):
# #     print(a+b)
# # def mul(a,b):
# #     print(a*b)
# # calculator()
# # sum(1,2)
# # mul(2,4)
# class calculator:
#
#     def __int__(self,a,b):
#         return a+b
#     print("done")
#
#     def mul(self,a,b):
#         return a*b
#     print("mul done")
#
#     def div(self,a,b):
#         return a/b
#     print("div done")
# obj=calculator()
# # print(obj.__int__(2,4))
# # print(obj.div(2,6))
# # print(obj.mul(3,7))
# print(obj.mul(2,4))


# class raveendra:
#     num=190
#
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#         print("gooo one get")
#
#     def new(self):
#         print("nottttt")
#
#
#     def sumval(self):
#         return self.a+self.b+self.num
#
# obj=raveendra()
# print(obj.new())
# print(obj.__int__(2,5))
# print(obj.sumval())
#
# #string split
#
# g1="sravendra@gmail.com"
# b1=g1.split(".")
# print(b1) # prints--['sraveendra@gmail' , 'com']
#
# g2="ravendra.samapathi.divya.100 crore money have"
# p=g2.split(".")
# print(p)

#exception raising
# r=int(input("enter the value:"))
# if r>=18:
#     pass
#
# assert(r>=18)

# r=int(input("enter the value:"))
# if r!=10:
#     raise Exception("not matched enterd value")

# items=20
# if items<15:
#     pass
# assert(items==10)

# items=0
# if items!=2:
#     raise Exception("valuie is not match")

# items=0
# if items!=2:
#     pass
# assert (items==2)

# try:
#     file=open("tex.txt",'r')
#     print(file.read())
# except Exception as e:
#     print(e)


# it=0
# if it!=2:
#     raise Exception("not given nunber")


# it=0
# if it!=2:
#     pass
# assert(it==2)

#Exception handle by used the try and except

# try:
#     it = 0
#     if it != 2:
#         pass
#
#     assert (it == 2)
#
# except Exception as e:
#     print(e)

# try:
#     with open('tr.txt','r') as reader:
#         print(reader.read())
#
# except Exception as e:
#     print(e)




#finally used the always below of the try and except
# try:
#     it=2
#     if it/0==0:
#         print("divisin by zero")
# except Exception as e:
#     print(e)
# finally:
#     print("shows the zero error and error is displayed")

# it=0
# if it!=2:
#     raise Exception("its not 2 in items")


# try:
#     it=0
#     if it!=2:
#         pass
#     assert(it==2)
# except Exception as e:
#     print(e)

# try:
#     it=2
#     if it/0==0:
#         print("not happen")
#     else:
#         print("its gone")
# except Exception as e:
#     print(e)









