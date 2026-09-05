"""
day = 98
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")

"""
"""
day = 9
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
  case _:
    print("Invalid day")
    """
"""
month = 4
day = 3
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    """

personality = {
    "name" : "Maryam",
    "age" : 15,
    "gender" : "female",
    "class" : 12,
    "course" : "Medicine"
}

import json
with open("personality.json" , "w") as f:
    json_string = json.dumps(personality, indent=4)
    f.write(json_string)

for i in range(6):
    print(i)


for j in range(2,6):
    print(j)

"""
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)
print(x.year)
print(x)
"""
print("x")
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

