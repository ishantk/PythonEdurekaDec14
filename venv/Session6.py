a = 10 # Global Variable

class Student:

    def hello(self):
        b = 100 # Local Variable to hello method
        print("a is:",a)
        print("b is:", b)

s1 = Student()
s1.hello()          # Translated to -> Student.hello(s1) | IMPLICIT CALL
Student.hello(s1)   # EXPLICIT CALL

s1.roll = 101
s1.name = "John"

print("a is:",a)
# print("b is:", b) error, since b is local to hello in class Student

# Printing data within Object pointed by s1
print(s1.__dict__)