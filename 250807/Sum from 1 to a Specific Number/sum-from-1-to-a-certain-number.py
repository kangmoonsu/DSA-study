n = int(input())

def sum(n):
    num = 0
    for i in range(1,n+1):
        num += i

    print(num//10)

sum(n)
