N = int(input())
arr = [int(input()) for _ in range(N)]

# 1, -1, -1, 1, -1,-1,-1,-1

max_num = 0
answer = 0
pos_num = 0
neg_num = 0

for i in range(N):
    if arr[i] > 0:
        pos_num += 1
        max_num = max(answer, pos_num)
        neg_num = 0
        answer = max(max_num, pos_num)
    elif arr[i] < 0:
        neg_num += 1
        max_num = max(answer, neg_num)
        pos_num = 0
        answer = max(max_num, neg_num)
print(answer)
        