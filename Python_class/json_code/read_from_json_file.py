import json

with open("/Users/rithyp/Documents/KIT_folder/Python_class/json_code/employees.json","r") as fp:

    #load without s because loads for string 
    dict_company_data = json.load(fp)

    for employee in dict_company_data["employees"]:
        print(employee["name"])


    