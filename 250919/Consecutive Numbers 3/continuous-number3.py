N = int(input())
arr = [int(input()) for _ in range(N)]

pos = 0
neg = 0

for i in range(N):
    if arr[i] < 0:
        neg += 1
    elif arr[i] > 0:
        pos += 1

print(max(pos,neg))
        