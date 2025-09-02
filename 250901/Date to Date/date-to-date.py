# m1, d1, m2, d2 = map(int, input().split())

# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# days = 0
# for i in range(m1+1,m2):
#     days += num_of_days[i]

# days += num_of_days[m1] - d1 + 1

# days += d2

# print(days)
# Variable declaration and input
m1, d1, m2, d2 = tuple(map(int, input().split()))


def num_of_days(m, d):
    # For calculation convenience, list the number of days in each month.
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # From January to (m - 1) month, all days are fully counted.
    for i in range(1, m):
        total_days += days[i]
    
    # For the month m, there are exactly d days.
    total_days += d
    
    return total_days    


# Output
total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
print(total_days)
