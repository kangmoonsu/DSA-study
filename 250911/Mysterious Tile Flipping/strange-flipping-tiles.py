n = int(input())
commands = [input().split() for _ in range(n)]

# We use a dictionary to keep track of the colors of the tiles.
# The key is the tile's position (an integer), and the value is its color ('W' for white, 'B' for black).
tiles = {}
current_position = 0

for num_str, direction in commands:
    num = int(num_str)
    
    if direction == 'L':
        # Move to the left and flip tiles to white.
        for i in range(num):
            tiles[current_position - i] = 'W'
        current_position -= (num - 1)
    elif direction == 'R':
        # Move to the right and flip tiles to black.
        for i in range(num):
            tiles[current_position + i] = 'B'
        current_position += (num - 1)

# Count the number of white and black tiles.
white_tiles = 0
black_tiles = 0

for color in tiles.values():
    if color == 'W':
        white_tiles += 1
    elif color == 'B':
        black_tiles += 1

print(white_tiles, black_tiles)