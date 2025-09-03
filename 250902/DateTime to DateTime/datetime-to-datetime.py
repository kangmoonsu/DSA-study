# Declare variables and take input
a, b, c = tuple(map(int, input().split()))

# Calculate the difference
diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

# Output
if diff < 0:
    print(-1)
else:
    print(diff)
