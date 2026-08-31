class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def grade(self, score):
        print(f"{self.name} scored {score} in the exam.")
        print("{} scored {} in the exam.".format(self.name, score))

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")
        print("Student Name: {}, Age: {}".format(self.name, self.age))
        