m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0

if m1 == m2:  # 같은 달인 경우
    days = d2 - d1 + 1
else:  # 다른 달인 경우
    # 중간 달들의 일수 합계
    for i in range(m1 + 1, m2):
        days += num_of_days[i]
    
    # 시작 달에서 남은 일수
    days += num_of_days[m1] - d1 + 1
    
    # 끝 달에서의 일수
    days += d2

print(days)
