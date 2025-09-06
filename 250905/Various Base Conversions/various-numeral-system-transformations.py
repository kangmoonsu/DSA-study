N, B = map(int, input().split())

if B == 4:
    result = ""
    while N > 0:
        remainder = N % 4
        result = str(remainder) + result
        N //= 4
    print(result)

elif B == 8:
    print(oct(N)[2:])
