n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
cur = 1

# 1 5 2 3 5 8 8
# 4

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 1

print(max(ans,cur))