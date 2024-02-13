# file=open('text.txt')
# print(file.read())
# file=open('text.txt','w')
# file.write("tinaa..../n")

# with open('text.txt','r') as reader:
#     print(reader.read())
# with open('text.tx','a') as app:
#     app.write("qdhtfcehm.../n")
#     app.write("yjdgjeukhk....")
# file=open('text.tx','r')
# for i in file.readlines():
#     print(i)

with open('text.tx') as reader:
    con=reader.readlines()
    reversed(con)
    with open('text.tx','w') as writer:
        for line in reversed(con):
            writer.write(line)