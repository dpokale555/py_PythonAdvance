#Exapmple 1: count function from itertools
from itertools import count

for i in count(3):
    print(i)
    if i>=20:
        break

#Exapmple 2: accumulate, takewhile function from itertools
from itertools import accumulate,takewhile

numbers1=list(accumulate(range(8)))
print(numbers1)
print(list(takewhile(lambda x:x<11,numbers1)))






