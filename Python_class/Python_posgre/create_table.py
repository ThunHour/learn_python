
import psycopg2

try: #if you dont connect to any database it will automaticlly connect to your posgres
    db_connect = psycopg2.connect(host = "localhost", port= "5432",database= "bank_acc", user="postgres",password="RithYP12345")

    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")


    cursor.execute("CREATE TABLE customer_info (c_id SERIAL, c_name VARCHAR(50), balance INTEGER);")
    db_connect.commit() #commit manulally
    print("Table created succesfully")

except Exception as error:
    print(error)

finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")