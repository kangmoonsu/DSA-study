n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

slot = [0] * (n+1)

for a, b in commands:
    for i in range(a, b + 1):
        slot[i] += 1

maxNum = max(slot)
print(maxNum)