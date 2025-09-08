n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

slot = [0] * 201

for a, b in segments:
    a, b = a + 100, b + 100
    for i in range(a, b):
        slot[i] += 1

maxNum = max(slot)

print(maxNum)