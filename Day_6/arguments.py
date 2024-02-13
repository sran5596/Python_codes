#positonal arguments
#keyword arguments

# def fun(i,j):
#     print(i+j)
# #fun(2,3) # positional arguments
# fun(j=3,i=2) # keyword arguments [here positon is not matter]

#deafult values passed
# def fun(i,j=10):
#     print(j,i)
# fun(2,3) #positional arguments
#fun(2) # its keyword and positional arguments combination
#if you not pass the two arguments it take the default value

#Keyword arguments
# def fun(name,greet):
#     print("welcome "+name+ greet)
# #fun("raveendra","hi") #positional
# fun(greet="udemy_py_se_pra",name="raveendra")

#remember always positonla arguments is before the kwyword arguments
# def fun(a,b,c):
#     print(a+b+c)
# fun(a=10,3,54)
#it show the error---SyntaxError: positional argument follows keyword argument

# try:
#     def fun(a, b, c):
#         print(a + b + c)
#
#
#     fun(a=10, 3, 54)
# except  Exception as e:
#     print(e)


# def fun(a,b):
#     print(a,b)
# fun(1,a=9) # it give the --TypeError: fun() got multiple values for argument 'a'

# function calling the inside the if
# def fun(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
# print(fun(200,300)) ##print (300,200)
# print(fun(100,50)) # print(100,50)
# function returns the multiple values its that case ___print tuple







