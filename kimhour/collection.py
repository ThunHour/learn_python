# Tuple ==> Immtable 
# def sumOfCollection(*num): #Tuple ==> *num
#     for i in num:
#         for j in i:
#             print(j)

# list1 = [500,800,50,25,45]
# dict1 = {123: "Kimhour",124: "Monirith", 125:"Ratanak"}

# sumOfCollection(list1,dict1)

def sumOfCollection(list_num):
    return sum(list_num)

print(sumOfCollection([50,60,100,85,65]))


#Collection
def ret_collection_from_fn(rangesNum):
    list1 = []
    for i in range(rangesNum):
        list1.append(i)
    return list1
    # return '\n'.join(map(str,list1)) show 1 as 1 in sepeate line

print(ret_collection_from_fn(5))




# def fetchrecords():
#     listOfUser = {123:"Kimhours", 134:"Severyvann",145:"Ratanank"}
#     return listOfUser

# print(fetchrecords())









