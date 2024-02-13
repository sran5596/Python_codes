a=10
b=10
c=20
print(id(a))
print(id(b))
print(id(c))
if print(id(a))==print(id(c)):
    print("yes")
# elif print(id(b))==print(id(c)):
#     print("el if")
else:
    print("No")