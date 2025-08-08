a, o, c = input().split()
a = int(a)
c = int(c)
r = 0

if o == "+":
    r = a+c
elif o == "-":
    r = a-c
elif o == "/":
    r = a//c
elif o == "*":
    r = a*c


print(a,o,c,"=",r)