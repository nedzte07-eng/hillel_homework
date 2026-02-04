class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def student_info(self):
        print(f"Звать {self.name}, призвіще {self.surname}, {self.age} рочків, має {self.average_grade} середній бал")

    def average_change(self, new_grade):
        self.average_grade = new_grade

sasha = Student('Sasha', 'Nedz', 41, 10)

print("Before change")
sasha.student_info()
sasha.average_change(12)
print("After change")
sasha.student_info()

