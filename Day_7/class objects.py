
#1)
# try:
#     class fun:
#         def fun1(self):
#             pass
#
#         def fun2(self, name):
#             print(name)
#
#
#     obj = fun()
#     obj.fun1()
#     obj.fun2("raveendra")
# except Exception as e:
#     print(e)

#2)
# class fun:
#
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#         print("good")
#
#     def fun1(self,name):
#         print(name)
#
#     def add(self):
#         return self.a+self.b
# obj=fun()
# obj.__int__(2,3)
# print(obj.add())

#3)
# class fun1:
#     def fun2(self):
#         pass
#     def fun3(self):
#         print("gova")
# obj=fun1()
# # print(obj.__init__())
# print(obj.fun3())

#Instance method
# class fun:
#     def fun1(self):
#         print("done")
# obj=fun()
# obj.fun1()
#this call only through to object

#static metjod
#annotation @staticmethod
# class fun1:
#     def fun2(self):
#         print("gova")
#     @staticmethod
#     def fun3(self,name):
#         print(name)
# obj=fun1()
# obj.fun3("welcome","raveendra")
#self also consider as argument

#class and global and local variables example
# x,y=10,20 # global variable
# class fun:
#     d,g=3,4 # class variable
#     def add(self,a,b): # local variables
#         print(a+b)
#         print(self.d+self.g)
#         print(x+y)
# obj=fun()
# obj.add(5,6)

#class and global and local variables but same all
#a,b=10,20
# class fun:
#     a,b,=30,40
#     def fun1(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         #print(a+b)
#         #same name all variables there so use below to get the global var
#         print(globals()['a']+globals()['b'])
# obj=fun()
# obj.fun1(5,6)

#Method and constructor example
# class demo:
#
#     def __init__(self):
#         print("its first")
#     def add(self,a,b):
#         return a+b
# obj=demo()
# print(obj.add(2,3))

# class demo1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("good")
#         print(a+b)
#     def add(self,i,o):
#         print(i+o)
# obj=demo1(5,6)
# obj.add(2,3)


# #emp table
# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#         print(eid,ename,sal)
#     def fun(self):
#         print(self.eid,self.ename,self.sal)
# obj=emp(1,"raveendra",2000000)
# obj.fun( )

#only string purpose prints used construcer
#__str__(self
# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#         # print(eid,ename,sal)
#     def __str__(self): # its for string type print purpose
#         return(self.ename)
#     # def fun(self):
#     #     print(self.eid,self.ename,self.sal)
# obj=emp(1,"raveendra",2000000)
# # obj.fun( )
# # print(obj)
# #print(obj.__str__())
# print(obj)# its invoke the total things


#used the __str__(self) for the string return purpose only
# try:
#     class fun:
#         def __init__(self,eid,ename,sal):
#             self.eid=eid
#             self.ename=ename
#             self.sal=sal
#             print(eid,ename,sal)
#         def __str__(self):
#             return(self.ename,self.eid)
#     obj=fun(1,"raveendra",12000000)
#     print(obj)
# except Exception as e:
#     print(e)
#
# finally:
#     print("done")
# #it printd the error -- [__str__ returned non-string (type tuple)]

#correct code for the __str__(self)
# try:
#     class fun:
#         def __init__(self, eid, ename, sal):
#             self.eid = eid
#             self.ename = ename
#             self.sal = sal
#             print(eid, ename, sal)
#
#         def __str__(self):
#             return (self.ename)
#
#
#     obj = fun(1, "raveendra", 12000000)
#     print(obj)
# except Exception as e:
#     print(e)
#
# finally:
#     print("done")

