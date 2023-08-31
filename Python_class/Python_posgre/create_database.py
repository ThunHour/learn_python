#Frist step install driver (psycopg2)

import psycopg2

#Connection to DBMS
try:
    #everything in try consider as transection, you need to commit for saving your data in DBMS
    db_connect = psycopg2.connect(host = "localhost", port= "5432", user="postgres",password="RithYP12345")

    db_connect.autocommit = True #commit automatically
    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")

    cursor.execute("CREATE DATABASE bank_acc") #Create database

except Exception as error:
    print(error)

finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")


