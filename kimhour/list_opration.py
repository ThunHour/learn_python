a = ["Java","C++","C#","C","Python","JS"]

a.append("Ruby")
print(a)



a.insert(2,"SQL")
print(a)

a.remove("C")
print(a)


del a[0:2]
print(a)


#list_add_to_list
a = ["Java","C++","C#","C","Python","JS"]

b = [1,2,3,4,5,6]

a.extend(b)
print(a)

a = ["Java","C++","C#","C","Python","JS"]
a.extend(["CSS","HTML","MySQL"])
print(a)

a = ["Java","C++","C#","C","Python","JS"]
a.append(["CSS","HTML","MySQL"])
print(a)







