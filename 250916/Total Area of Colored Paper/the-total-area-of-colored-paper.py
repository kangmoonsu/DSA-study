n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

grid = [[False] * 201 for _ in range(201)]

for i in range(n):
    px, py = x[i], y[i]
    for dx in range(8):
        for dy in range(8):
            nx, ny = px + dx + 100, py + dy + 100
            if 0 <= nx < 201 and 0 <= ny < 201:
                grid[nx][ny] = True

area = sum(sum(row) for row in grid)
print(area)
