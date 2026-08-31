class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grade(self, score):
        print(f"{self.name} scored {score} in the exam.")
        #print("{} scored {} in the exam.".format(self.name, score))

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")
        #print("Student Name: {}, Age: {}".format(self.name, self.age))

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student1.grade(95)
student1.display_info()

student2.grade(88)
student2.display_info()

