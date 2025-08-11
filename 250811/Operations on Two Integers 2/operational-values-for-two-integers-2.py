a, b = map(int, input().split())

if a > b: 
    a = a * 2
    b = b + 10
else:
    a = a + 10
    b = b * 2

print(a,b)