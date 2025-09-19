n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 1
current_cnt = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        current_cnt += 1
        max_cnt = max(max_cnt, current_cnt)
    else:
        current_cnt = 1

print(max_cnt)
