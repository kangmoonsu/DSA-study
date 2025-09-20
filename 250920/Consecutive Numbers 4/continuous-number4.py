n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
max_n = 0



for i in range(n-1):
    if n == 1:
        ans = 1
    elif arr[i] < arr[i+1]:
        ans += 1
    else:
        max_n = 1

print(max(ans,max_n))