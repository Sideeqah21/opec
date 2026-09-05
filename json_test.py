import json
students = []
while True:
    try:
        Name = input("Enter your name : ")
        Age = int(input("Enter your age : "))
        Favourite_subject = input("What is your best subject ?  ")

        student = {
        "name" : Name,
        "age" : Age,
        "Fave_subj" : Favourite_subject
        }


        with open("student_history.json" , "r") as f:
            history = json.load(f)
            students.append(history)

        with open("student_history.json" , "w") as f:
            json.dump(history, f, indent=4)
        

        print("Student: ", history["name"])
        print("Age: " , history["age"])
        print("Favourite subject: ", history["Fave_subj"])   

        break


    except (ValueError):
        print("hey! Please enter a valid age in numbers only.")

    