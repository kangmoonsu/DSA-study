a, b = map(int, input().split())
n = input()

digits = []

num = 0
for ch in n:
    num = num * a + int(ch)

# Convert to base b.
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")
