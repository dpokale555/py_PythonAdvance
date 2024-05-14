def add_ten(x):
    return x+10

def twice(fun, arg):
    return fun(fun(arg))

print(twice(add_ten,5))
