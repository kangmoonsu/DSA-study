n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
for i in range(n):
    print(arr[i], end = ' ')