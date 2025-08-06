n = int(input())

def f(n):
    a = 1
    for i in range(n):
        for i in range(n):
            print(a, end=" ")
            a += 1
            if a == 10:
                a = 1
        print()
        
f(n)