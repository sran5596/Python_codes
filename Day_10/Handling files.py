# #writing the data  on file
# writer=open("D:\pythonfileshandling\myfile.txt",'w')
# writer.write("Samapthi../n")
# writer.write("raveendra.../n")
# writer.write("divya........./n")
# writer.write("srann......./n")
# writer.write("rakan..../n")
# writer.close()

#reading the file
# reader=open("D:\pythonfileshandling\myfile.txt",'r')
# #print(reader.read())
# print(reader.readline(5))
# for line in reader.readlines():
#     print(line)
#reader.close

#add more the data along with existing data next
# with open("D:\pythonfileshandling\myfile.txt",'a') as add:
#     add.write("this added through to append../n")

#scenario
# with open("D:\pythonfileshandling\myfile.txt") as reader:
#     con=reader.readlines()
#     reversed(con)
#     with open("D:\pythonfileshandling\myfile.txt","w") as writer:
#         for line in reversed(con):
#             writer.write(line)

#it reverse the total data
# with open("text.txt") as reader:
#     con=reader.readlines()
#     reversed(con)
#     with open("text.txt","w") as writer:
#         for line in reversed(con):
#             writer.write(line)

# read=open('text.txt','r')
# print(read.readlines())
# print(read.read())
# reader=open('text.txt')
# li=reader.readlines()
# reversed(li)
# writer=open('text.txt',"w")
# for line in reversed(li):
#     writer.write(line)






