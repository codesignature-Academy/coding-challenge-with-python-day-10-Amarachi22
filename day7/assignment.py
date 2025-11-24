def add(a,b):
    return a + b
a = int(input('type a number: '))
b = int(input('type a number: '))

sol = add(a,b)
print("the sum of a and b is",sol)



def subtract(a,b):
    return a - b
sol = subtract(a,b)
print( "the difference between a and b is",sol)


def multiply(a,b):
    return a * b
sol = multiply(a,b)
print("the product of a and b is",sol)

def divide(a,b):
    return a / b
sol = divide(a,b)
print("a divided by b is",sol)

def square(a,b):
    return a ** b
sol = square(a,b)
print("a raised to the power of b is",sol)
