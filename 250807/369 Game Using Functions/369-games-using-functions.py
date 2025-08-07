a, b = map(int, input().split())

def contains_digit(num, digits):
    """숫자가 특정 자릿수들(3, 6, 9) 중 하나를 포함하는지 확인"""
    while num > 0:
        if num % 10 in digits:
            return True
        num //= 10
    return False

def cnt(a, b):
    count = 0
    target_digits = {3, 6, 9}
    
    for i in range(a, b + 1):
        # 3의 배수이거나 3, 6, 9 중 하나의 자릿수를 포함하면 카운트
        if i % 3 == 0 or contains_digit(i, target_digits):
            count += 1
    
    return count

print(cnt(a, b))
