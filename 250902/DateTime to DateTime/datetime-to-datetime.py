a, b, c = map(int, input().split())

if b < 11 or (b == 11 and c < 11):
    total = -1
else:
    total = (a - 11) * 60 * 24 + (b - 11) * 60 + (c - 11)

print(total)    

