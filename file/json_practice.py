"""
import json

json_data = '{"name" : "Aisha", "age" : 17, "subjects" : ["Maths","Physics","Chemistry"]}'

py_obj = json.loads(json_data)
print(py_obj["name"])
print(py_obj["age"])
print(py_obj["subjects"])
print(py_obj)

"""
import json
genius = {

    "name": "Maryam",
    "age" : 15,
    "subjects" : ["Biology","Chemistry","Physics","English"]
}

mod_girl = json.dumps(genius)
print(mod_girl)

with open("students.json" , "w") as file:
    json.dump(genius,file, indent = 4)

with open("students.json" , "r") as file:
    data = json.load(file)
print(data)
print(data["name"])
print(data["subjects"][2])
