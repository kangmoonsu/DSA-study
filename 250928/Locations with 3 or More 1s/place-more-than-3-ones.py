n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(n):
        adjacent_ones = 0
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                adjacent_ones += 1
        
        if adjacent_ones >= 3:
            count += 1

print(count)
