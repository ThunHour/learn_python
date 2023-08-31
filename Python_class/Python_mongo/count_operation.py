import pymongo

cilent = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create db or open db
db = cilent["employee"]

#go to collection or create collection
collection = db["employee"]


#will count how many record in your collection
collection_count = collection.count_documents({})
print(collection_count)