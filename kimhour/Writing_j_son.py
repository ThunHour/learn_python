import json
my_json_data = '''
    { 
        "employee":[
            {
                "name":"Kim hour",
                "age": 20,
                "school": "KIT",
                "is_studying":true,
                "family":[{
                    "member":4,
                    "mother name": "so Pheap",
                    "father name" : "kheang",  
                    "Older brother name" : "khav"
                    }]
                },
            {
                "name":"china",
                "age":18,
                "School":"KIT",
                "isStudying":true,    
                "family":"dun know"    
            },           
            {
                "name":"Seanghor",
                "age":20,
                "School":"KiT",
                "is_studying": true,
                "family":"dun know"
            }
        ]
    }
'''

my_dict = json.loads(my_json_data)

for i in my_dict["employee"]:
    del i["family"]
print(my_dict)

my_json_data=json.dumps(my_dict,indent=3,sort_keys=True)
print(my_json_data)
