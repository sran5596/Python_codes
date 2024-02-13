# from Day_9.modulespackegs import cal
#
#
# class one(cal):
#     num1=120
#     def __init__(self):
#         cal.__init__(self,3,4)
#
#     def sum(self,r,y):
#         self.r=r
#         self.y=y
#         print(self.num+self.num1)
# obj=one()
# obj.sum(3,4)

# from Day_9.modulespackegs import *
# add(6,8)
# mul(6,8)

#super keyword used to print the parent method print statement
# class ravi:
#     def fun1(self):
#         print("fun1")
# class ravi1(ravi):
#     def fun1(self):
#         print("fun2")
#         super().fun1()
# obj=ravi1()
# obj.fun1()


# class ra:
#     name="rave"
# class ra1(ra):
#     name="tina"
#     def test(self):
#         print(super().name)
# obj=ra1()
# print(obj.name)
# obj.test()

#hirarchy inheritance
# class bank:
    # def bankrate(self):
    #     return 0
# class ybank(bank):
#     def bankrate(self):
#         return 10
#     def test(self):
#         print(super().bankrate())
# class xbank(bank):
#     def bankrate(self):
#         return 12
# obj=ybank()
# print(obj.bankrate())
# obj.test()
#
# obj1=xbank()
# print(obj1.bankrate())

# #Day_9 have the modulepackegs $ modulecalling import functions
# from Day_9.modulespackegs import *
# fly()
# color()
# from Day_9.modulecalling import *
# color()
# fly()

# from Day_9.a import hu
# obj=hu()
# obj.fun2()
# from Day_9.b import ani
# obj=ani()
# obj.fun1()
#
# from Day_9.modulespackegs import add#,mul
# add(2,6)
# try:
#     from Day_9.modulespackegs import fly,color
#     fly()
#     color()
#     from Day_9.modulecalling import fly,color
#     fly()
#     color()
# except Exception as e:
#     print(e)
# try:
#     r=int(input("enter the value:"))
#     while r<=2:
#         raise Exception ("its not two")
#
# except Exception as e:
#     print(e)

# list=0
# if list!=2:
#     pass
# assert(list!=0)
from Day_9.a import hu
obj=hu()
obj.fun2()