#normal case
# import time
# print(time.time())
# def square(numbers):
#     for i in numbers:
#         time.sleep(0.2)
#         print(i*i)
#
# print(time.time())
# one=time.time()
# def cube(numbers):
#     for i in numbers:
#         time.sleep(0.2)
#         print(i*i*i)
# two=time.time()
# numbers=[1,2,3,4,5,6,7,8,9,10]
# s1=square(numbers)
# s2=cube(numbers)
# print(s1)
# print(s2)
#
# print(two+one)
#Threading
# import time
# import threading
#
# def square(numbers):
#     for i in numbers:
#         time.sleep(0.2)
#         print(i*i)
# def cube(numbers):
#     for i in numbers:
#         time.sleep(0.2)
#         print(i*i*i)
#
# numbers=[1,2,3,4,5,6,7,8,9,10]
# t1=threading.Thread(target=square,args=(numbers,))
# t1.start()
# t2=threading.Thread(target=cube,args=(numbers,))
# t2.start()
# print(time.time())

# import time
# import threading
# print(time.time())
#
# def one(l):
#     for i in l:
#         time.sleep(0.2)
#         print(i*2)
# time.time()
# print("firstone:",time.time())
# def three(l):
#     for i in l:
#         time.sleep(0.2)
#         print(i*3)
# # print(time.time())
# l=[1,2,3,4,5,6,7,8,9,10]
# t1=threading.Thread(target=one,args=(l,))
# t1.start()
# t2=threading.Thread(target=three,args=(l,))
# t2.start()
# print(time.time())



