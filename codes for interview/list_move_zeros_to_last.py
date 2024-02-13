lists=[2,0,8,6,0,3,5,0]
for i in lists:
    if i==0:
        lists.remove(i)
        lists.append(i)
print(lists)