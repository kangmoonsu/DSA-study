a, b = map(int, input().split())

def prime(a,b):
    psum = 0
    for i in range(a,b+1):
        cnt = 0
        for d in range(1, i+1):
            if i % d == 0:
                cnt += 1
        if cnt == 2:
            psum += i

    return psum

print(prime(a,b))