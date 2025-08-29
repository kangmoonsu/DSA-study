unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Op:
    def __init__(self, c,w,s):
        self.c = c
        self.w = w
        self.s = s


op1 = Op(unlock_code,wire_color,seconds)

print("code :", op1.c)
print("color :", op1.w)
print("second :", op1.s)