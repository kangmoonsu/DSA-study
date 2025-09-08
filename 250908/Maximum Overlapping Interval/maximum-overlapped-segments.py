n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

slot = [0] * 100

for a, b in segments:
    for i in range(a, b + 1):
        slot[i] += 1

maxNum = max(slot)

print(maxNum)