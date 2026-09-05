with open("file.txt", "w") as f:
    f.write("First line of text\n")
    f.write("Second line of text\n")
    f.write("Third line of text\n")



with open("file.txt", "r") as f:
    num = 1    
    for fil in f:
        print(f"{num} : {fil.strip()}")
        num += 1



try:
    with open("scores.txt", "r") as file:
        for line in file:
            username, score = line.strip().split(",")
            score = int(score)  # Convert to int
            print(f"{username}: {score}")
except FileNotFoundError:
    print("Scores file not found!")
except ValueError:
    print("Invalid score format in file!")