n = int(input())
arr = list(map(int, input().split()))

def even(arr):
    for idx, val in enumerate(arr):
        if val % 2 == 0:
            arr[idx] = val // 2

even(arr)

print(*arr)
