# Class declaration
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


# Variable declaration and input
n = int(input())
students = []
for _ in range(n):
    name, korean, english, math = tuple(input().split())
    students.append(Student(name, int(korean), int(english), int(math)))

# Sorting using a custom comparator
students.sort(key = lambda x: (-x.korean, -x.english, -x.math))

# Output
for student in students:
    print(student.name, student.korean, student.english, student.math)
