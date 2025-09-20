n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 1

# 1 5 2 3 5 8 8
# 4
for i in range(n-1):
    if n == 0:
        ans = 1
    elif arr[i] < arr[i+1]:
        ans += 1
    else:
        ans = 1

print(ans)