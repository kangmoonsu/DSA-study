n = int(input())
blocks = [int(input()) for _ in range(n)]

avg = sum(blocks) // n
ans = 0
for i in range(n):
    if blocks[i] > avg:
        ans += blocks[i] - avg

print(ans)
