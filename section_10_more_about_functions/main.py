# we assigned a default value to b that can be overwritten
def area(a, b=6):
    return a * b


print(area(5), ": we passed a=5 and used default b=30 value")
print(area(a=4, b=3), ": we keyword-assigned value to a and overwritten value for b")


# function with variable ammount of arguments
def foo(*args):
    return sum(args) / len(args)


print(foo(1, 2, 3, 4, 5, 6), ": variable ammount of args")


# function with variable ammount of keyword arguments
def foo2(**kwargs):
    return kwargs


print(foo2(a=1, b=2, c=3), "this is printed using keyword args")
