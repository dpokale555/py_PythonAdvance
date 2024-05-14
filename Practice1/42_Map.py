# Example 1: Map allows us to do operate on a list or perform single operation on a given list.
def add_number(x):
    return x+5

mylist1 =[10,20,30,40]

result=list(map(add_number,mylist1))
print(result)

#Example 2: same example 1 using lambda
mylist2=[1,2,3,4]
print(list(map(lambda x:x+5,mylist2)))

