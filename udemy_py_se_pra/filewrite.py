# file=open("D:/pythonprograms/udemy_py_se_pra/text.txt","w")
# file.write("read data")
# file.write("\n")
# file.write("get data")
# file.write("\n")
# file.write("herooo")
# file.write("\n")
# file.write("jooo")
# file.close()
# file=open("D:/pythonprograms/udemy_py_se_pra/text.txt","r")
# # print(file.read())
# # for i in file.readlines():
# #     print(i)
# # print(file.readline())
# print(file.read(2))
# with open("D:/pythonprograms/udemy_py_se_pra/text.txt","w") as file:
#     file.write("/n")
#     file.write("ravee")
#     file.write("\n")
#     file.write("ndra")
# with open ("D:/pythonprograms/udemy_py_se_pra/text.txt","a") as file:
#     file.write("/n")
#     file.write("ravee")
#     file.write("\n")
#     file.write("ndra")
# with open("D:/pythonprograms/udemy_py_se_pra/text.txt","r") as file:
#     one=file.readlines()
#     reversed(one)
#     with open("D:/pythonprograms/udemy_py_se_pra/text.txt","w") as file:
#         for i in reversed(one):
#             file.write(i)
# with open("D:/pythonprograms/udemy_py_se_pra/text.txt","r") as file:
#     one=file.readlines()
#     reversed(one)
#     with open("D:/pythonprograms/udemy_py_se_pra/text.txt","w") as file:
#         for line in reversed(one):
#             file.write(line)
# cart=int(input("enter the cart items:"))
# if cart!=2:
#     # raise Exception("cart is not wqual to 2")
#     assert cart==2 ,"cart is not wqual to 2"
# import openpyxl
# workbook=openpyxl.load_workbook("D:\Datasets\d1.xlsx")
# sheet=workbook["Sheet1"]
# columns=sheet.max_column
# rows=sheet.max_row
# for r in range(1,rows+1):
#     for c in range(1,columns+1):
#         print(sheet.cell(r,c).value,end=" ")
#     print()
try:
    with open("/udemy_py_se_pra/text.txt", "r") as file:
        one=file.readlines()
        reversed(one)
        with open("/udemy_py_se_pra/text.txt", "w") as file:
            for i in reversed(one):
                file.write(i)
except Exception as e:
    print(e)
finally:
    with open ("/udemy_py_se_pra/text.txt", "a") as file:
        file.write("/n")
        file.write("gooooooooooo")
        file.write("\n")
        file.write("herooooooooooo")





