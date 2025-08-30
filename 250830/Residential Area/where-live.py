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

last_person = max(people_list, key=lambda person: person.n)

# Please write your code here.
print("name",last_person.n)
print("addr",last_person.a)
print("city",last_person.r)