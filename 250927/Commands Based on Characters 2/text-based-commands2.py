# Variable declaration and input
dirs = input()
x, y = 0, 0
curr_dir = 3

# Define dx, dy in the order of East, South, West, North.
dxs = [1,  0, -1, 0]
dys = [0, -1,  0, 1]

# Proceed with the movement.
for c_dir in dirs:
    # Rotate 90' counterclockwise
    if c_dir == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    # Rotate 90' clockwise
    elif c_dir == 'R':
        curr_dir = (curr_dir + 1) % 4
    # Move forward
    else:
        x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x, y)
