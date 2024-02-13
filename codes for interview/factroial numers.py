num=5
sum=1
if num<0:
    print("NO FACTORIAS")
elif num==0:
    print("zero factorial is 1")
else:
    for i in range(1,num+1):
        sum=sum*i
    print(sum)