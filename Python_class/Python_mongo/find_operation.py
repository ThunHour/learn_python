import pymongo

cilent = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create db or open db
db = cilent["employee"]

#go to collection or create collection
collection = db["employee"]
#if you want to find something
results = collection.find({"Name" : "Monirith"})
# print(results) #<pymongo.cursor.Cursor object at 0x7fa77ee8c2e0> not useful


# #if you dont want to see something like this you can
for result in results:
    print(result) #{'_id': ObjectId('60fda3a97aac5ded75e1d761'), 'id': 1, 'Name': 'Monirith', 'score': 10}

    print(result["score"]) # 10


#It print all your data in collection
# results = collection.find({})
# for result in results:
#     print(result) 