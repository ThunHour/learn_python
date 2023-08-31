import psycopg2

try: #if you dont connect to any database it will automaticlly connect to your posgres
    db_connect = psycopg2.connect(host = "localhost", port= "5432",database= "kit_b9", user="postgres",password="RithYP12345")

    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")

    cursor.execute("SELECT * FROM student_marks;") #You can put condition like WHERE s_id = 2 

    # records = cursor.fetchall() #Will give you all the record in table

    record = cursor.fetchone() #Will give you only the first record in your table 

    #It will give you all your record line by line 
    # for record in records:
    #     print(record)


except Exception as error:
    print(error)

finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")