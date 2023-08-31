import pymongo

cilent = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create db or open db
db = cilent["employee"]

#go to collection or create collection
collection = db["employee"]

#it will delete record which id ==1
# results = collection.delete_one({"id":1})


#to delete everything in collection
results = collection.delete_many({})
