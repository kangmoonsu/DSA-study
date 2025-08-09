n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_same(n):
    for i in range(n2):
        if a[i + n] != b[i]:
            return False

    return True


# Check if b is a contiguous subsequence of a.
def is_subsequence():
    for i in range(n1 - n2 + 1):
        if is_same(i):
            return True
    
    return False


if is_subsequence():
    print("Yes")
else:
    print("No")