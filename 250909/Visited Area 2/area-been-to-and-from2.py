n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

offset = 100
path = [0] * 201
current_pos = offset

for i in range(n):
    step = x[i]
    direction = dir[i]

    if direction == "R":
        for j in range(current_pos, current_pos + step):
            path[j] += 1
        current_pos += step
    elif direction == "L":
        for j in range(current_pos - step, current_pos):
            path[j] += 1
        current_pos -= step

visited_twice_count = 0
for count in path:
    if count >= 2:
        visited_twice_count += 1

print(visited_twice_count)