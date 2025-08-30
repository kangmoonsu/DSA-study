n = int(input())

class Person:
    def __init__(self, n, a, r):
        self.n = n
        self.a = a
        self.r = r

people_list = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    p = Person(n_i,s_i,r_i)
    people_list.append(p)

# Please write your code here.
print("name",people_list[n-1].n)
print("addr",people_list[n-1].a)
print("city",people_list[n-1].r)