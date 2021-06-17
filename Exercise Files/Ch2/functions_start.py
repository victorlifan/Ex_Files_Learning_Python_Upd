#
# Example file for working with functions
#

# define a basic function
def func1():
    print('func1')

# function that takes arguments


def func2(a, b):
    print(a, b)

# function that returns a value


def func3(a, b):
    return a+b

# function with default value for an argument


def func4(a=1, b=2):
    return a+b

# function with variable number of arguments


def func5(*a):
    r = 0
    for i in a:
        r += i
    return r
