
import psycopg2

try: #if you dont connect to any database it will automaticlly connect to your posgres
    db_connect = psycopg2.connect(host = "localhost", port= "5432",database= "bank_acc", user="postgres",password="RithYP12345")

    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")

    c_name = input("Input your name: ")
    balance = int(input("Input your balance: "))

    #If you do something like this VALUES ('Dinesh' 100) ==> it is hard since 
    # if you need to insert other record you need to errase it and put it again
    # cursor.execute("INSERT INTO student_mark(s_name, mark) VALUES ('Dinesh', 100)") 

    cursor.execute("INSERT INTO customer_info (c_name, balance) VALUES (%s, %s);",(c_name, balance))
    db_connect.commit()
    print("Record inserted sucessully")
    
except Exception as error:
    print(error)

finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")