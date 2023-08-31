import json

company_json_data  = '''
    {
        "employees":
        [
            {
                "name":"Huot Monirith",
                "age":30,
                "position":"CTO",
                "salary":"4000$",
                "come_from":"Phnom Penh",
                "working_duration":10
            },

            {
                "name":"Seak Kimhours",
                "age":20,
                "position":"Mobile Developer",
                "salary":"2000$",
                "come_from":"Phnom Penh",
                "working_duration":5
            },

            {
                "name":"Hai senghour",
                "age":20,
                "position":"Web Developer",
                "salary" :"1000$",
                "come_from":"Phnom Penh",
                "working_duration":2
            },

            {
                "name":"Kim Sereyvath",
                "age":24,
                "position":"Business Analysis",
                "salary":"3000$",
                "come_from":"Kompong chang",
                "working_duration":5
            }
        ]


    }
'''

print(company_json_data) #string 

#to conver it to dict to read 
dict_company_data = json.loads(company_json_data)

#To print all the name in dict
for employee in dict_company_data["employees"]:
    print(employee["name"])
    del (employee["age"]) #Delete "age" from employess
    employee["Huot Monirith"] = "Monirith" #Update value 


#covert it back to JSON 
my_json_data = json.dumps(dict_company_data, indent=3 ,sort_keys= True)
print(dict_company_data)
print(my_json_data)

