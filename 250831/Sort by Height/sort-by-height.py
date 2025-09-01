# Class declaration
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight


# Variable declaration and input
n = int(input())
students = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), int(weight)))

# Sorting using a custom comparator
students.sort(key = lambda x: x.height)

# Output
for student in students:
    print(student.name, student.height, student.weight)
