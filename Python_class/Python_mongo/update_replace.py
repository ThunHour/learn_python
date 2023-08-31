import pymongo

cilent = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create db or open db
db = cilent["employee"]

#go to collection or create collection
collection = db["employee"]

#Will update name ==> Monirith to Huot Monirith
# results = collection.update_one({"id": 1},{"$set": {"name":"Huot Monirith"}})


#rename column record
# results = collection.update_one({"id":1},{"$rename":{"score":"points"}})
