# l1=["raveendra","sampathi"]
# l1[0]="rave"
# print(l1)

# di={}
# di[0]=True
# print(type(di))
# print(di)
# di["name"]="sampathi"
# print(di)

#sum of sirst five natural numbers
# sum=0
# for i in range(1,6):
#     sum=i+sum
# print(sum)
# s="rave"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# print(s[::-1])

# r=int(input("enter the:"))
# t=int(input("enter the:"))
# sum=0
# while t<=r:
#     sum=sum+t
#     t=t+1
# print(t)

# def ca():
#     print("goo")
# def add(a,b):
#     return a+b
#     print("se goo")
# def mul(v,n):
#     return v*n
#     print("th goo")
# # ca()
# print(add(3,7))
# print(mul(2,4))

# def cal(name):
#     print("welcome"+name)
# cal("raveendra")

# class calculater:
#     num=200
#
#     def add(self):
#         print("add one")
#
#     def mul(self):
#         print("mul sec")
#
# obj=calculater()
# obj.add()
# obj.mul()

# class calculater:
#     num=200
#
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#         print("its called first")
#
#     def goo(self):
#         print("second")
#
#     def add(self):
#         return self.a+self.b+self.num
#
# obj=calculater()
# obj.__int__(2,4)
# obj.goo()
# print(obj.add())

# r=int(input("enter the value:"))
# t=int(input("neter :"))
# sum=0
# while r<=t:
#     sum=sum+r
#     r+=1
# print(sum)
# sum=0
# for i in range(1,6):
#     sum=i+sum
#     print(sum)

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)

# s="sampathiraveendra"
# print(s.split("i"))

# s="           yfdgqwiukj           "
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# file=open('t.txt')
# file.read()
#file read
# file=open('te.txt')
# print(file.read())

# with open('te.txt','r') as reader:
#     con=reader.readlines()
# #     print(con)
# file=open('te.txt','w')
# # print(file.read())
# print((file.write("jiva")))

#read method
# file=open('te.txt','r')
# # print(file.read()) # it give all elements
# # print(file.read(2)) # it give only two leters
# s=print(file.readlines()) # it give list type data
# for i in s:
#     print(s[::-1])

# with open('te.txt','r')as reader:
#     print(reader.read())

#write data in file
# file=open('te.txt','w')
# file.write("siva")

# with open('te.txt','w') as writer:
#     writer.write("sreenu")

#add more values
# file=open("D:\pythonprograms\Udemypractise\te.txt","a")
# file.append("naripi")

# with open('te.txt') as reader:
#     r=reader.read()
#     reversed(r)
#     with open("te.txt",'w')as writer:
#         for i in reversed(r):
#             writer.write(i)

# line=open('te.txt')
# d=line.readline()
# while d!=0:
#     print(d)
#     d=line.readline()
# file=open('te.txt')
# for i in file.readlines():
#     print(i)

# file=open('te.txt')
# line=file.readline()
# while line!=" ":
#     print(line)
#     line=file.readline()
# line.close()

# lu=[1,2,8,4,5]
# sum=0
# for i in lu:
#     sum=sum+i
# print(sum)
# sum=0
# for i in range(1,6):
#     sum=sum+i
#     print(sum)
# print(sum)
# lu.sort()
# print(lu)
# print(lu.index(4))
# file=open('te.txt')
# c=file.readline()
# while c!=" ":
#     print(c)
#     c=file.readline()
#
# file.close()

# file=open('D:\pythonprograms\Udemypractise\te.txt','r')
# print(file.read())
# with open('te.txt','a') as app:
#     app.write(("ravi"))
    # with open('te.txt','r') as reader:
    #     print(reader.read())

# with open('te.txt',"r") as reader:
#     p=reader.readlines()
#     print(p)
# file=open('te.txt','r')
# # print(file.read())
# for i in file.readlines():
#     print(i)




