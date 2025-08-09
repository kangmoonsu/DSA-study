n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_contiguous_subsequence(A, B):
    
    n1 = len(A)  # A의 길이
    n2 = len(B)  # B의 길이
    
    # B가 A보다 길면 불가능
    if n2 > n1:
        return False
    
    # A의 각 위치에서 시작해서 확인
    for i in range(n1 - n2 + 1):  # 시작 가능한 위치들
        # i번째 위치부터 B와 같은지 확인
        match = True
        for j in range(n2):
            if A[i + j] != B[j]:
                match = False
                break
        
        # 일치하면 True 반환
        if match:
            return True
    
    return False

if is_contiguous_subsequence(a, b):
    print("Yes")
else:
    print("No")
# def is_same(n):
#     for i in range(n2):
#         if a[i + n] != b[i]:
#             return False

#     return True


# # Check if b is a contiguous subsequence of a.
# def is_subsequence():
#     for i in range(n1 - n2 + 1):
#         if is_same(i):
#             return True
    
#     return False


# if is_subsequence():
#     print("Yes")
# else:
#     print("No")