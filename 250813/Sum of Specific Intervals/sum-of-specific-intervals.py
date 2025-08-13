N, M = map(int, input().split())
A = list(map(int, input().split()))

# 6 4
# 6 5 4 3 2 1
# 1 2
# 2 4
# 3 4
# 5 6

for _ in range(M):
    a1, a2 = map(int, input().split())
    result = sum(A[a1-1:a2])
    print(result)