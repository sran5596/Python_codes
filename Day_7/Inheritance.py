#single inheritance --
# class fun1: #parent
#     def met1(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
# obj=fun1()
#
# class fun2(fun1): # child
#     def met2(self,q,w):
#         self.q=q
#         self.w=w
#         print(q-w)
#         print(self.a*self.b)
# obj=fun2()
# obj.met1(2,3)
# obj.met2(2,4)

#multi level inheritance
# class cal: #parent
#     def add(self,a,b):
#         global f
#         f=10
#         self.a=a
#         self.b=b
#         return a+b
#
# class cal1(cal): # child
#     def mul(self,q,w):
#         self.q=q
#         self.w=w
#         return q*w
# class cal2(cal1): #grand child
#     def sub(self,s,d):
#         self.s=s
#         self.d=d
#         return f-d
# obj=cal2()
# print(obj.add(2,3))
# print(obj.mul(4,5))
# print(obj.sub(6,7))

# #heirarchy inheritance
# class sam: # parent
#     def fun1(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
# class rav(sam): # first child
#     def fun2(self,t,u):
#         self.t=t
#         self.u=u
#         print(self.a*self.t)
# class dev(sam): # second child
#     def fun3(self,y,i):
#         self.y=y
#         self.i=i
#         print(self.y-y)
# obj1=rav()
# obj1.fun1(3,5)
# obj1.fun2(6,8)
#
# obj2=dev()
# obj2.fun3(5,7)
# obj2.fun1(7,6)

# #multiple inheritance
# class multiple: #father
#     def fun1(self,a,b):
#         self.a=a
#         self.b=b
#         return a*b
# class multiple1: # mother
#     def fun2(self,q,w)
#         self.q=q
#         self.w=w
#         return q-w
# class mul(multiple,multiple1): # child
#     def fun3(self):
#         return self.a+self.w
#
# obj=mul()
# print(obj.fun2(3,4))
# print(obj.fun1(2,5))

#static methods
# class ravi:
#     s=100
#     def r1(self):
#         print("good")
#
#     @staticmethod
#     def r2(self,a):
#
#
#
#         print(a)
# obj=ravi()
# obj.r1()
# obj.r2(2,3)

