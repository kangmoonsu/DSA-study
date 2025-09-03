m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

total = 0
if m1 == m2:
    date = (d2-d1)//7
else:
    for i in range (m1,m2):
        total += num_of_days[i]
    total -= d1
    total += d2
    date = total//7

print(days[date])