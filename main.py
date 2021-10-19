class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Section :", self.section)


p1 = Person("Sanket", "21")
p1.display()
print("----------------------------------")
s1 = Student("Bhushan", "21", "BTECH-02")
s1.displayStudent()
