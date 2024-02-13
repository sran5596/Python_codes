# try:
#     print(y)
# except Exception as e:
#     print(e)
# finally:
#     print("done")
# try:
#     num=int(input("enter the value: "))
#     print(num/0)
# except Exception as e:
#     print(e)
# try:
#     num=int(input("enter the value: "))
#     num1=int(input("enter the value: "))
#     print(num/num1)
# except ZeroDivisionError:
#     print("zerodivision is handled")
# except SyntaxError:
#     print("syntax is handled")
# except Exception as e:
#     print(e)
# except :
#     print("no exception")
# else:
#     print("no exception is occured")
# finally:
#     print("completed")
# try:
#     def fun(num):
#         if num>0:
#             raise ValueError("only int accepted")
#         if num%2==0:
#             raise Exception("sloved")
#         else:
#             print("done")
# except Exception as e:
#     print(e)

# def num(num):
#     if num/0:
#         raise ZeroDivisionError("accept the more than the zero")
#     if num%2==0:
#         print("even")
# num(10)