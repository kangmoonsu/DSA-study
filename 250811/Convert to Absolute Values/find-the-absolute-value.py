n = int(input())
arr = list(map(int, input().split()))

def abs_val(arr):
    for i in arr:
        print(abs(i), end = ' ')


abs_val(arr)