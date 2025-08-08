a, o, c = input().split()
a = int(a)
c = int(c)
r = 0

def operate(a,o,c):
    if o == "+":
      r = a+c
    elif o == "-":
        r = a-c
    elif o == "/":
        r = a//c
    elif o == "*":
        r = a*c
    else:
        return False


print(operate(a,o,c))