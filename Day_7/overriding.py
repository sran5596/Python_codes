
#accessing the global and class and local variables
# a,b=1,2
# class fun:
#     a,b=3,4
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
# obj=fun()
# obj.add(8,9)


#method overriding

#super keyword usage
#parent and child have the same methods that time it print the parent method
# class f1:
#     def m1(self):
#         print("a is parent of b")
# class f2(f1):
#     def m1(self):
#         print("b is parent of a")
#         super().m1() # it prints parent print statement also
#
# obj=f2()
# obj.m1()

# #variable overriding
# class fun1:
#     name="Sampathi"
#
# class fun2(fun1):
#     name="Raveendra"
#     def test(self):
#         print(super().name)
#
# class fun3(fun2):
#     name="sam srann"
# obj=fun3()
# print(obj.name)
# obj.test()
#

#overriding the methods -- Here used the hirarchy model one parent and two childs
# class bank:
#     def rateofinterst(self):
#         return 0
# class xbank(bank):
#     def rateofinterst(self):
#         return 10
#         print(super().bank())
#
# class ybank(bank):
#     def rateofinterst(self):
#         return 12
#
# obj=xbank()
# print(obj.rateofinterst())
# # print(obj.rateofinterst())
#
# obj1=ybank()
# print(obj1.rateofinterst())
#
# class y:
#     def m1(self):
#         print("a ony b")
# class r(y):
#     def m1(self):
#         print("b only a")
#         super().m1()
# ob=r()
# ob.m1()

# class fun:
#     name="raveendra"
# class fun1(fun):
#     name="Sampatghi"
#     def test(self):
#         print(super().name)
# obj=fun1()
# print(obj.name)
# obj.test()


