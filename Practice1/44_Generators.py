#Gemnerators are kind of list but with some diffrence
#Example 1:
def fun():
    counter= 0
    while counter <5:
        yield counter
        counter+=1

for x in fun():
    print(x)

#Example 2: generate the list of even number
def even_num(x):
    for i in range(x):
        if i % 2 ==0:
            yield i

print(list(even_num(25)))


