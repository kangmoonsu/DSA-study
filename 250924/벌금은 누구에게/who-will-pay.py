N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

student.sort()
cnt = 1
for i in range(M-1):
    if student[i] == student[i+1]:
        cnt += 1
        if cnt >= K:
            print(student[i])
            break
    else:
        cnt = 1
else:
    print(-1)
