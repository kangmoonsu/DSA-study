N = int(input())

def one(N):
    if N == 1:
        return 0
    elif N % 2 == 0:
        return one(N//2) + 1
    else:
        return one(N//3) + 1


print(one(N))