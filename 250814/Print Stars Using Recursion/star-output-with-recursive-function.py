n = int(input())

def stars(n):
    star = "*"
    for i in range(n):
        print(star)
        star+="*"

stars(n)