n = int(input())
nums = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

for i in range(n):
    print(nums[i], end=' ')
print()
for i in range(n-1,-1,-1):
    print(nums[i], end=' ')