import time
def listsort(l):
    print("before:",time.time())
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=[10,5,8,3,9,1]
sort=listsort(l)
print(sort)
one=time.time()
print(one)

def listsort2(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=[10,5,8,3,9,1]
sort2=listsort2(l)
print(sort2)
time1=time.time()

print("time:",time1+one)

