n = int(input())
arr = list(map(int, input().split()))


for i in range(n):
    if i % 2 == 0:
        # Perform ascending sort.
        sorted_arr = sorted(arr[:i + 1])
        # Print the middle value.
        print(sorted_arr[i // 2], end=" ")