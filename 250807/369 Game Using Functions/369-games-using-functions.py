a, b = map(int, input().split())

def cnt(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i // 10 == 3 or i % 10 == 3:
            cnt += 1
        elif i // 10 == 6 or i % 10 == 6:
            cnt += 1
        elif i // 10 == 9 or i % 10 == 9:
            cnt += 1
        elif i % 3 == 0:
            cnt += 1
    return cnt

print(cnt(a,b))
        