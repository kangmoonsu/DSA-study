secret_code, meeting_point, time = input().split()
time = int(time)

class s007:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

op = s007(secret_code, meeting_point, time)

print("secret code : " + op.secret_code)
print("meeting point : " + op.meeting_point)
print("time : " + str(op.time))