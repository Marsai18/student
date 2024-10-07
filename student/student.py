class Student:
    _next_registration_number = 1

    def __init__(self, name):
        self.name = name
        self.registration_number = Student._next_registration_number
        Student._next_registration_number += 1  # Increment for the next student

    def display_info(self):
        return f"Student Name: {self.name}, Registration Number: {self.registration_number}"


student1 = Student("masai")
student2 = Student("Absalom")

print(student1.display_info())
print(student2.display_info())
