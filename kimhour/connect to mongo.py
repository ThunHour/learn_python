try:
    import pymongo

    client=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb=client["b9"]

    student=mydb["KIT_student"]

    data={'id':31,'name':'sovankoko','age':22}

    student.insert_one(data)
    print('completed')
except Exception as e:
    print('error',e)
