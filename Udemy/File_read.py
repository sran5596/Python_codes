# def raveendra():
#     print("gooo")
# def verygood():
#     print("best")
# def sum(a,b):
#     print(a+b)
# raveendra()
# verygood()
# sum(4,3)

# class calculator:
#     b=10
#
#     def __init__(self,v1,v2):
#         self.v1=v1
#         self.v2=v2
#         print("its always first")
#
#     # def sum(self):
#     #     return self.v1+self.v2+self.b
#
#     def mul(self):
#         print("mul is")
#
#     def sum(self):
#         return self.v1+self.v2+self.b
#
#
# obj=calculator(3,6)
# # print(obj.__init__(6 , 8))
# print(obj.sum())
# print(obj.mul())

##################################### main ###########################

# file=open("text.txt")
#print(file.read()) # it print all data
#print(file.read(15)) # it print 15 elements only here [space] also consider the element
# print(file.readline())
# print(file.readline())
#readline code is print the elemnts line by line

##############################################################
#interview question#
########################################
#print all lines one by one use loops it print all
# line=file.readline()
# while line!="":
#     print(line)
#     line=file.readline()
#
#
# ###########0r#################
# for i in file.readlines():
#     print(i)

# file=open('text.txt')
# print(file.readlines())

## read the all line by line
## reverse the list
## write the book list on file
# with open('text.txt','r') as reader: # file=open('text.txt') alter native with started
#     con=reader.readlines()
#     reversed(con) # it reverse the list
#     with open('text.txt','w') as writer:
#         for line in reversed(con):
#             writer.write(line)

# with open('text.txt') as reader:
#     con=reader.readlines()
#     fun=con[::-1]
#     with open('text.txt',"w") as writer:
#         for i in fun:
#             writer.write(i)

# with open('text.txt') as reader:
#     good=reader.readlines()
#     reversed(good)
#     with open('text.txt','w') as writer:
#         for line in reversed(good):
#             writer.write(line)

#####only read
# with open('text.txt','r') as reader:
#     reader.reradlines()
# file=open('text.txt')
# con=file.readlines()
# print(con)
# print(con[::-1])

# with open('text.txt','r') as reader:
#     print(reader.read()) # all
#     print(reader.readline()) # single element

####write only
# # with open("text.txt",'w') as writer:
#     writer.write("sampathi")
# with open('text.txt','r') as reader:
#     don=reader.readlines()
#     reversed(don)
#     with open('text.txt',"w") as writer:
#         for line in reversed(don):
#             writer.write(line)




