N, M, K = map(int, input().split())
student = [0] * (N+1)  

for _ in range(M):
    num = int(input())
    student[num] += 1  

for i in range(1, N+1):
    if student[i] >= K:
        print(i)
        break
else:
    print(-1)
