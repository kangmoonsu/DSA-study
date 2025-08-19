a, b, c = map(int, input().split())

multi = a*b*c

def mulSum(multi):

    if multi == 0:
        return 0
    
    return mulSum(multi//10) + multi%10

print(mulSum(multi))