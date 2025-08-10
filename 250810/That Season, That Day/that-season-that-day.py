y, m, d = tuple(map(int, input().split()))


def is_leap_year(y):
    # If it's not a multiple of 4, it is definitely not a leap year.
    if y % 4 != 0:
        return False
    
    # At this point, we can assume it is a multiple of 4.
    # If it is not a multiple of 100, it is definitely a leap year.
    if y % 100 != 0:
        return True
    
    # At this point, we can assume it is a multiple of 100.
    # If it is a multiple of 400, it is definitely a leap year.
    if y % 400 == 0:
        return True
    
    # At this point, it is a multiple of 100 but not a multiple of 400.
    # Therefore, it is definitely not a leap year.
    return False


def is_exist_day(y, m, d):
    #                  1. 2.  3. 4.  5    6.  7.  8.  9. 10. 11  12
    num_of_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle leap year processing.
    num_of_days[2] = 29 if is_leap_year(y) else 28

    # d should not exceed the maximum number of days in the month.
    return d <= num_of_days[m]

   
# If the date y-m-d does not exist, print -1.
if not is_exist_day(y, m, d):
    print(-1)
else:
    # If the date y-m-d exists, print the season corresponding to the month.
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    else:
        print("Winter")
