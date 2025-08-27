user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class user:
    def __init__(self,id,level):
        self.id = id
        self.level = level

user1 = user("codetree",10)
user2 = user(user2_id,user2_level)

print("user",user1.id,"lv",user1.level)
print("user",user2.id,"lv",user2.level)
    