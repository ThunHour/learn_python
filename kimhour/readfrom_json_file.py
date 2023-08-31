import json

#Deserialize =>reading from a json file into python java php etc
with open("employee_data.json","r")as file:
    my_dict=json.load(file)
    print(my_dict)
    for employee in my_dict["employee"]:
        print(employee["name"])
