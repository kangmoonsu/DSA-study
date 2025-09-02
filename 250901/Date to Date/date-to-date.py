m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(m1+1,m2):
    days += num_of_days[i]

days += num_of_days[m1] - d1 + 1

days += d2

print(days)
