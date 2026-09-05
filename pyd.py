from pydantic import BaseModel, Field

"""class User(BaseModel):
    name: str
    age: int  
    email: str      
 

user = User(
    name = "Maryam",
    age = 18,
    email = "maryam@example.com"
)

print(user.name)
print(user.age)
print(user.email)"""


"""class Doctor(BaseModel):
    name: str
    specialty: str
    email: str

    def introduce(self):
        print(f"Hello, I am Dr. {self.name} and a {self.specialty} specialist. Here is my email : {self.email}")

doctor1 = Doctor(
    name="Smith",   
    specialty="Cardiology",
    email="smith@example.com"

)
doctor2 = Doctor(
    name="Johnson",
    specialty= "Neurology",      
    email="johnson@example.com"
)

doctor1.introduce()
x = doctor1.name
print(x)
doctor2.introduce()
y = doctor2.specialty
print(y)
z = doctor2.email
print(z)"""


"""class Patient(BaseModel):
    name: str
    age: int
    email: str
    phone: str | None = None

patient1 = Patient(
    name="Sofia",
    age=16,
    email="sofia@example.com",
    phone="123-456-7890"
)
patient2 = Patient(
    name="Ali",
    age=20,
    email="ali@example.com"
)   
print(patient1.name)
print(patient1.phone)
print(patient2.name)
print(patient2.phone)"""

"""class Product(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(ge=0)
    quantity: int = Field(ge = 1 , le=100)

product1 = Product(
    name="Laptop",
    price=999.99,
    quantity=10
)   

print(product1.name)
print(product1.price)
print(product1.quantity)"""

"""class Patient(BaseModel):
    name: str = Field(... , min_length=2)
    name: str = Field(... , min_length=2)
    email: str 
    phone: str | None = None

patient1 = Patient(
    name="Sofia",
    age=16,
    email="sofia@example.com",
)

print(patient1.name)
print(patient1.phone)"""

"""class Doctor(BaseModel):
    name: str
    specialty: str

class Appointment(BaseModel):
    patient_name: str
    doctor: Doctor
    date: str | None = None

appointment = Appointment(
    patient_name="Sofia",
    doctor= Doctor(
        name="Smith",
        specialty="Cardiology"
        ),
    date="2023-07-15"
)

print(appointment.doctor.name)
print(appointment.doctor.specialty)"""

from pydantic import BaseModel, Field, ValidationError

class Test(BaseModel):
    name: str = Field(..., min_length=2)

try:
    Test(name="A")
except ValidationError as e:
    print(e.errors()[0]["msg"])