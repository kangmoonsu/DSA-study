a, b = map(int, input().split())

def primeAndSum(a,b):
    answer = 0
    for i in range(a,b+1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt+=1
        if cnt <= 2:
            if ((i // 10) + (i % 10)) % 2 == 0:
                answer+=1

    return answer

print (primeAndSum(a,b))
        

        