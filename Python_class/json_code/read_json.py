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

#to conver it to dict (loads)
dict_company_data = json.loads(company_json_data) #s ==> convert into dictionary
print(dict_company_data)
#To print all the name in dict
for employee in dict_company_data["employees"]:
    print(employee)
    print(employee["name"])

print("== == == == == == == == == == == ")
for employee in dict_company_data["employees"]:
    print(employee["age"])
