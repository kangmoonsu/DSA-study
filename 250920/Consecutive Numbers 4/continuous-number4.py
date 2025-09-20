n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
cur = 1

# 1 5 2 3 5 8 8
# 4

for i in range(n-1):
    if arr[i] < arr[i+1]:
        cur += 1
    else:
        max(ans, cur)
        cur = 1

print(max(ans,cur))