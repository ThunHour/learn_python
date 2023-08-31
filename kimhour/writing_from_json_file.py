import json

with open("employee_data.json", "r") as file:
    my_dict = json.load(file)
    file.close()
with open("employee_data.json","w") as fp:
    json.dump(my_dict,fp,indent=4,sort_keys=True)
    print(my_dict)
fp.close()
