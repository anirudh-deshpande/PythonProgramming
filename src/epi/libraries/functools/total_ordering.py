class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        return (self.firstname, self.lastname) == (other.firstname, other.lastname)

    def __lt__(self, other):
        return (self.firstname, self.lastname) < (other.firstname ,other.lastname)


student1 = Student("Bond", "James")
student2 = Student("Haddok", "Captain")

# Where are these coming from?
print(student2 > student1)  # True
print(student2 >= student2) # True
print(student2 != student1) # True