text = input()
pattern = input()

# codetree
# ee
def substr(t,p):
    if pattern in text:
        return text.index(pattern)
    else:
        return -1

print(substr(text,pattern))