M, D = map(int, input().split())


mon30 = [4,6,9,11]
mon31 = [1,3,5,7,8,10,12]

def year2021(M,D):
    if M == 2:
        if D <= 28:
            return True
        else:
            return False
    elif M in mon30:
        if D <= 30:
            return True
        else:
            return False
    elif M in mon31:
        if D <= 31:
            return True
        else:
            return False
    else:
        return False

if year2021(M,D):
    print("Yes")
else:
    print("No")
# 2
# 4 6 9 11 
# 1 3 5 7 8 10 12
