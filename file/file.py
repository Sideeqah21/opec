#r = Read
#a = Append
#w = Write
#x = Create 
"""
a = open("test.txt")
print(a.read())

b = open("ex.txt")
print(b.read()) 
"""

#file = open("hospital.txt", "w")
#file.write("Welcome")
#file.close()

#file = open("hospital.txt", "a")
#file.write("\nHello, to the hospital!")
#file.close()
"""
with open("hospital.txt", "w") as file:
    file.write("Maryam")
    file.write("\nAli")
    file.write("\nHassan")
    file.write("\nAyesha")


with open("hospital.txt", "r") as file:
    print(file.read())

with open("hospital.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("hospital.txt", "r") as file:
    print(file.readlines())
"""

with open("patent.txt", "w") as file:
    file.write("Maryam")
    file.write("\nAli")
    file.write("\nHassan")
    file.write("\nAyesha")

with open("patent.txt", "r") as file:
    for line in file:
        print("Patient line:", line)

        
