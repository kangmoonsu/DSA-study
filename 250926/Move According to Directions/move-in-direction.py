n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

x,y = 0, 0
for i in range(n):
    if dir[i] == 'N':
        y += dist[i]
    elif dir[i] == 'E':
        x += dist[i]
    elif dir[i] == 'W':
        x -= dist[i]
    elif dir[i] == 'S':
        y -= dist[i]
        
print(x,y)