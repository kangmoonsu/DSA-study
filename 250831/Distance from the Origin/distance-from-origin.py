# Variable declaration and input:
n = int(input())
distances = list()


# Function to calculate the distance from the origin.
def get_dist_from_origin(x, y):
    return abs(x) + abs(y)


for i in range(n):
    x, y = tuple(map(int, input().split()))
    # Store the distance from the origin and the index.
    distances.append((
        get_dist_from_origin(x, y), i + 1
    ))

distances.sort()

for _, idx in distances:
    print(idx)
