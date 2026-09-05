import json

user = {
    "name": "Maryam",
    "age": 18,
    "student": True
}

with open("user.json", "w") as file:
    json.dump(user, file)

with open("user.json", "r") as file:
    data = json.load(file)
    print(data)