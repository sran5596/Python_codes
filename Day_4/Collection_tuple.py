#creating the tuple
# 1)orderd and unchangable
# 2)use-()
# 3)immutable

#creating the tuple
t1=("raveendra",True,1,5.6)
print(t1)
t2=("raveendra",True,1,5.6)
print(t2)
print(id(t1))
print(id(t2))

# access the itmes on tuple
print(t1[3]) # index used
print(t1[::-1])
print(t1[-1])
print(t1[2:4])
print(type(t1))
t3=list(t1)
print(type(t3))
t3.append("sampathi")
print(t3)
t3.insert(2,"gova")
print(t3)
t1=tuple(t3)
print(type(t1))
print(t1)

#reading the values use for loop
for i in t1:
    print(i)

#check the values is there or not
if "gova" in t1:
    print("yes")
else:
    print("goo")

# adding and updates not have chance in tuple
#length of the tuple
print(len(t1))

#deleting the tuple itmes
print(t1)

# y1=("ravi")
# del y1
# print(y1)
# print(type(y1))

# join two table
r1=(1,2,3)
r2=("r","t","d")
o=(1,2,3)
g=r1+r2
print(g)
# compaare two tuple
if r1==r2:
    print("eql")
else:
    print("no")
if r1==o:
    print("eql")
else:
    print("no")



