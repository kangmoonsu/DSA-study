n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cur = 0

for i in range(n-1):
    if arr[i] > t:
        ans += 1
        cur = max(ans,cur)
    else:
        ans = 0

print(max(ans,cur))