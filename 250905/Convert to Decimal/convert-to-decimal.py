binary = input()

num = 0
l = [int(d) for d in binary]
for i in l:
    num = num * 2 + i

print(num)

# binary = input()

# print(int(binary, 2))
