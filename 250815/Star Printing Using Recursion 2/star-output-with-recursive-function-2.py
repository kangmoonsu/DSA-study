n = int(input())

def stars(n):
    if n == 0:
        return

    for i in range(n):
        print("*", end = ' ')
    print()

    stars(n-1)

    for i in range(n):
        print("*", end = ' ')
    print()

stars(n)