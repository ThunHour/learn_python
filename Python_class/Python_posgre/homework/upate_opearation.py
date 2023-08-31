import psycopg2

try: #if you dont connect to any database it will automaticlly connect to your posgres
    db_connect = psycopg2.connect(host = "localhost", port= "5432",database= "bank_acc", user="postgres",password="RithYP12345")

    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")

    cursor.execute("UPDATE customer_info SET c_name = 'Seanghor' WHERE c_id = 4;")

    db_connect.commit()
    print("Record already updateed sucessully")
except Exception as error:
    print(error)

finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")