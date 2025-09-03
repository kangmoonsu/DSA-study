a, b, c = map(int, input().split())

total = (a - 11)*60*24
total += (b-11)*60

if b < 11 or (b == 11 and c <= 11):
    total = -1
elif b == 11:
    total += c-11
else:
    total += c+49

print(total)    

