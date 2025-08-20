n = int(input())

def sequence(a):
    if a == 1:
        return 2
    if a == 2:
        return 4

    return (sequence(a - 1) * sequence(a - 2)) % 100


print(sequence(n))
