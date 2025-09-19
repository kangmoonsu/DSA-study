N = int(input())
arr = [int(input()) for _ in range(N)]

max_num = 0
pos_num = 0
neg_num = 0

for i in range(N):
    if arr[i] < 0:
        neg_num += 1
        max_num = max(pos_num, neg_num)
    elif arr[i] > 0:
        pos_num += 1
        max_num = max(pos_num, neg_num)
print(max_num)
        