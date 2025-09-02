m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(m1+1,m2,+1):
    days += num_of_days[i]

d1 = num_of_days[m1] - d1

days += d1 + d2 + 1

print(days)
