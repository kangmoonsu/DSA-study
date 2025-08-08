# Variable declaration and input:
a, o, c = input().split()
a = int(a)
c = int(c)

# Write a function that returns the sum of two numbers.
def plus(a, b):
    return a + b

# Write a function that returns the value of a minus b.
def minus(a, b):
    return a - b

# Write a function that returns the product of two numbers.
def times(a, b):
    return a * b

# Write a function that returns the remainder of a divided by b.
def divide(a, b):
    return a // b


if o == '+':
    print(a, "+", c, "=", plus(a, c))
elif o == '-':
    print(a, "-", c, "=", minus(a, c))
elif o == '*':
    print(a, "*", c, "=", times(a, c))
elif o == '/':
    print(a, "/", c, "=", divide(a, c))
else:
    print("False")
