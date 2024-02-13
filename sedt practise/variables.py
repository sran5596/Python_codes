# glo_var=20
# def var():
#     # local_var=25
#     global local_var
#     local_var=30
#     print(glo_var*local_var)
# var()
# print(type(glo_var))
#
# glo=20
# def sam(a,b):
#     print(glo+b)
#     a=20
# sam(3,6)
# #positional arguments
# def sum(i,j):
#     if i>j:
#         print(i,j)
#     else:
#         print(j,i)
# sum(3,5)
# #keyword arguments
# def sum1(a,b=10):
#     print(a+b)
# sum1(10,6)
# def sum2(x,y,z=8):
#     print(y,x,z)
# sum2(4,5)

# class cal:
#     global one
#     one=20
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("this is first always")
#     def sum(self):
#         print(self.a*one)
#         return(self.b,one)
# obj=cal(2,6)
# print(obj.sum())
# class ravi:
#     def one(self,a,b):
#         print(a+b)
#     @staticmethod
#     def ravi1(self,v,c):
#         print(v+c)
# obj=ravi()
# obj.one(2,3)
# ravi().ravi1(self,3,4)
# list=['a','v','i','n','o']
# list.sort()
# print(list)
