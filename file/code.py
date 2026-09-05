while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    if __name__ == "__main__":
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                name = input("Enter student name: ")
                grade = float(input("Enter student grade: "))
                with open("students.txt", "a") as f:
                    f.write(f"{name},{grade}\n")
                print("Student added successfully.")
            except ValueError:
                print("Invalid grade. Please enter a valid number.")
        elif choice == "2":
            try:
                with open("students.txt", "r") as f:
                    students = f.readlines()
                if students:
                    print("\nList of Students:")
                    for student in students:
                        