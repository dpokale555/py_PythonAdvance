#Example1: To print the square of number
def square(x):
    return x**2
print(square(4))
print(square(int(input())))

#Do same by using lambda
result=(lambda x: x**2)(30)
print(result)

#####OR in one line############
result=(lambda x: x**2)(int(input()))
print(result)

#####OR in single line############
print((lambda x:x+10)(int(input())))