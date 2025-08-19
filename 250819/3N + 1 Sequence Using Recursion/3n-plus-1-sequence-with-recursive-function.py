n = int(input())

def pro(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return pro(n//2) + 1
    else:
        return pro(n*3+1) + 1

print(pro(n))
       