import psycopg2

try: #if you dont connect to any database it will automaticlly connect to your posgres
    db_connect = psycopg2.connect(host = "localhost", port= "5432",database= "bank_acc", user="postgres",password="RithYP12345")

    print("connection succeed")
    
    cursor = db_connect.cursor()
    print("Cursor received")


    debit_acc = int(input("Input the account to be debited: ")) #someone give money to other
    credit_acc = int(input("Input the account to be credited: ")) #someone receive money from other

    amount = int(input("Input the amount to be transferred: "))

    #reduce amount of money from debit_acc
    cursor.execute("UPDATE customer_info SET balance = balance - %s WHERE c_id = %s;", (amount,debit_acc))
    print(f"Sucessfully debited from account number {debit_acc}")
    #Add amount of money to credit_acc
    cursor.execute("UPDATE customer_info SET balance = balance + %s WHERE c_id = %s;", (amount,credit_acc))
    print(f"Sucessfully credited to account number {credit_acc}")


    db_connect.commit()
    print("Amount transfer success...")

except Exception as error:
    print(error)
    db_connect.rollback() #back to previous state

    print("Something went wrong rolling back to previous stage")
finally:
    cursor.close()
    db_connect.close()
    print("Cursor closed")
    print("Connection closed")