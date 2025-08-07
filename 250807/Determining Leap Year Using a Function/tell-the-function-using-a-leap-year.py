y = int(input())

def leap(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

if leap(y):
    print("true")
else:
    print("false")