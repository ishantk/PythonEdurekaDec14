class Student:

    def __init__(self, roll, name, phone):
        self.roll = roll
        self.name = name
        self.phone = phone
        print(">> Object Created")

    def __del__(self):
        print(">> Object Deleted")

    def studentToCSV(self):
        csv = "{},{},{}\n".format(self.roll, self.name, self.phone)
        return csv


s1 = Student(101, "John Watson", "+91 99999 88888")
s2 = Student(201, "Fionna Flynn", "+91 99999 77777")

print("Data for s1:")
print(s1.__dict__)

print("Data for s2:")
print(s2.__dict__)

# When our python program finishes execution we can say process is finished
# Hence, data in the memory is lost !! i.e. Objects are deleted from memory !!
# destructor __del__ is executed before object is deleted from memory !!
# In order to persist the data, we can write data in file !!

# w is write mode
# a is append mode
# file = open("students.csv", "w")  # data will be overwritten in file
file = open("students.csv", "a")    # data will be appended in file
data = s1.studentToCSV()
file.write(data)
data = s2.studentToCSV()
file.write(data)

print(">> Data Written in File !!")

# write() is an API !! -> Its a Built In Code !! We are just using it !!
# what write API is doing -> Explore the definition !!
# Refer Python Documentation

