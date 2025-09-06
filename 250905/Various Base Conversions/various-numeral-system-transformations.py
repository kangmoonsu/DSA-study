def solve():
    N, B = map(int, input().split())

    if B == 4:
        # Convert decimal to base 4
        if N == 0:
            print("0")
            return

        result = ""
        while N > 0:
            remainder = N % 4
            result = str(remainder) + result
            N //= 4
        print(result)

    elif B == 8:
        # Convert decimal to base 8
        print(oct(N)[2:])

if __name__ == "__main__":
    solve()