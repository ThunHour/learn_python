import pymongo

cilent = pymongo.MongoClient()

#create db or open db
db = cilent["employee"]

#go to collection or create collection
collection = db["employee"]


# for 1 record

# #write record
# recrod= {"_id": 1, "Name": "Monirith", "score": 10}

# #insert record into db
# collection.insert_one(recrod)


#for many record
record1 = {"id": 1, "Name": "Monirith", "score": 10}
record2 = {"id": 2, "Name": "Monipisey", "score": 20}
record3 = {"id": 3, "Name": "Zass", "score": 40}
collection.insert_many([record1,record2,record3])

