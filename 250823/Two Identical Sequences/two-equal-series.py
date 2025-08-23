n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
def checkSeq(n):
    num = 0
    for i in range(n):
        if A[i] != B[i]:
            num += 1
    return num

if checkSeq(n) == 0:
    print("Yes")
else:
    print("No")


