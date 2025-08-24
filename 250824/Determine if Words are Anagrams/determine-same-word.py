word1 = input()
word2 = input()

word11 = sorted(word1)
word22 = sorted(word2)



def check(word1,word2):
    for e1, e2 in zip(word1, word2):
        if e1 != e2:
            return False
    return True

if check(word11,word22):
    print("Yes")
else:
    print("No")
