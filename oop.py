"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

patient2 = User("Sofia", 16)
x = patient2.name
y = patient2.age
print(x,y)
"""

class Doctor:
    def __init__(self, name, specialty,email):
        self.name = name
        self.specialty = specialty
        self.email = email

    def introduce(self):
        print(f"Hello, I am Dr. {self.name} and a {self.specialty} specialist. Here is my email : {self.email}")

doctor1 = Doctor("Smith", "Cardiology", "smith@hospital.com")
doctor2 = Doctor("Johnson", "Neurology", "johnson@hospital.com")

doctor1.introduce() 
doctor2.introduce()