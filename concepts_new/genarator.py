def count_to_be(n):
    num=1
    while num<=n:
        yield num # it converst the value to generator
        num+=1
for numbers in count_to_be(20):
    print(numbers)
