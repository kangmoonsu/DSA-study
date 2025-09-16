x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

min_x = min(x1[0], x1[1], x1[2])
max_x = max(x2[0], x2[1], x2[2])
min_y = min(y1[0], y1[1], y1[2])
max_y = max(y2[0], y2[1], y2[2])

width = max_x - min_x
height = max_y - min_y

plane = [[0 for _ in range(width)] for _ in range(height)]

for i in range(x1[0] - min_x, x2[0] - min_x):
    for j in range(y1[0] - min_y, y2[0] - min_y):
        plane[j][i] = 1

for i in range(x1[1] - min_x, x2[1] - min_x):
    for j in range(y1[1] - min_y, y2[1] - min_y):
        plane[j][i] = 1

for i in range(x1[2] - min_x, x2[2] - min_x):
    for j in range(y1[2] - min_y, y2[2] - min_y):
        plane[j][i] = 0

result = 0
for i in range(height):
    for j in range(width):
        result += plane[i][j]

print(result)
