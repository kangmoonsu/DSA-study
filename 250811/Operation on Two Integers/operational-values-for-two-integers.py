a, b = map(int, input().split())

minn = min(a,b)
maxn = max(a,b)

minn = minn*2
maxn = maxn+25

print(minn,maxn)