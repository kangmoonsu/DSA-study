# m1, d1, m2, d2 = map(int, input().split())

# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# total = 0
# if m1 == m2:
#     date = (d2-d1)%7
# elif m1 > m2:
#     for i in range (m2,m1):
#         total += num_of_days[i]
#     total -= d2
#     total += d1
#     date = total%7
# else:
#     for i in range (m1,m2):
#         total += num_of_days[i]
#     total -= d1
#     total += d2
#     date = total%7

# print(days[date])
m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def days_from_start(month, day):
    """1월 1일부터 해당 날짜까지의 일수 계산"""
    total = 0
    for i in range(1, month):
        total += num_of_days[i]
    total += day - 1  # 1월 1일을 0일로 기준
    return total

# 각 날짜를 1월 1일부터의 일수로 변환
start_days = days_from_start(m1, d1)
end_days = days_from_start(m2, d2)

# 두 날짜 사이의 차이 계산
diff = end_days - start_days

# 7로 나눈 나머지로 요일 결정
day_index = diff % 7
print(days[day_index])
