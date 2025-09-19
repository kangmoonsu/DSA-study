n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

cnt = 0
for i in range(len(arr)-1):
    if len(arr) == 1:
        cnt = arr[0]
    elif arr[i] == arr[i+1]:
        cnt += 1
    elif arr[i] != 0:
        cnt = 0

print(cnt)