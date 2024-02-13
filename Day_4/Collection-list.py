# list=[1,"ravi",True,4.9]
# list1=["banan","apple","gun"]
# list2=[4,7,8,9]
# list3=[]
# print(type(list))
# list.insert(2,"raveendra")
# print(list)
# list[4]="yuva"
# print(list)

#Accessing the values in list
# print(list1[2])
# print(list2[-1])

# r="yifyuusg"
# # sum=""
# # for i in r:
# #     sum=i+sum
# # print(sum )
# print(r[::-1])
# i=int(input("enter the no:"))
# r=int(input("enter the no:"))
# sum=0
# while r<=i:
#     sum=sum+i
#     r=r+1
# print("sum of",sum)
# som=0
# for i in range(1,6):
#     som=som+i
#     print(som)
# n=5
# r=1
# som=0
# while r<=n:
#     som=som+r
#     r+=1
#     print(som)

#Range of indexes
# list=[3,6,"tina",True,False,8.9]
# print(list[1:3])
# print(list[-3:-1])

#Change the values in list
# list=["raveendra",1,3,8.9,True]
# list[1]="ravi"
# print(list)

#print all on console use thge loop
# for i in list:
#     print(i)

# check the item is there or not using ths conditional statements
# if "raveendra" in list:
#     print("y")
# else:
#     print("no")

#range of list
#print(len(list))

# list.pop(1)
# print(len(list))
# del list[2]
# print(list)

#Adding new itme
#append()-Index not need
#insert()-index need
#extend()-index not need it adds the nested list
# list=[6,8,"tina",True]
# list.append("goodone")
# list.append(["eva","hina"])
# print(list)
# list.insert(0,"god")
# print(list)
# list.extend(["revi","gova"])
# print(list)

#remove the items
#pop()- its function - based on index it removed
#del - Its keyword -based on index it removed
#clear()--its function - not need the index
# list=["raveendra",5,9,9.8,True]
# print(list)
# list.pop(1)
# print(list)
#
# del list[2]
# print(list)
# r1=["rvosuv",87]
# r1.clear()
# print(r1)

#Coping the list items
#list() -- s=list(s1)-syntax to copy ther list
#copy() ---s2=s.copy()- syntax to copy list
# s=["raveendra","ravikuamr"]
# s1=list(s)
# print(s1)
# print(s)
# s3=s1.copy() #another way to copy the list
# print(s3)

# Adding the two lists
# using the + operator
# using the for loop to add it
# extend also use
# list1=["ravi"]
# list2=["sampathi"]
# l3=list1+list2
# print(l3)
#
# for i in list2:
#     list1.append(i)
#     print(list1)
#
# list1.extend(list2)
# print(list1)


# for i in range(1,5):
#     for j in range(i):
#         if i%j==0:
#             print(j)

#compare the two lists
# list1=[1,2,3]
# list2=[1,2,3]
# if list1==list2:
#     print("eql")
# else:
#     print("not")

# t1=["raveendra",3,5]
# t1.remove(3)
# print(t1)
