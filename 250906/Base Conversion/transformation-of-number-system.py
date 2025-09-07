a, b = map(int, input().split())
n = input()

def base_conversion(a, b, n):
   
    # n을 10진법으로 변환
    decimal_n = 0
    for digit in str(n):
        decimal_n = decimal_n * a + int(digit)
    
    # 10진법 n을 b진법으로 변환
    result = ""
    while decimal_n > 0:
        remainder = decimal_n % b
        result = str(remainder) + result
        decimal_n //= b
    
    return result

print(base_conversion(a, b, n))
