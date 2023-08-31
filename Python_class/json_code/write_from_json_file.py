import json

with open("/Users/rithyp/Documents/KIT_folder/Python_class/json_code/employees.json","r") as fp:

    dict_company_data = json.load(fp)

    for employee in dict_company_data["employees"]:
        del employee['age']


    fp.close()

with open('/Users/rithyp/Documents/KIT_folder/Python_class/json_code/employees.json','w') as fp:
    json.dump(dict_company_data,fp, indent=3, sort_keys=True)
