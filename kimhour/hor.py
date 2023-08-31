import psycopg2
print("="*30, "Create Database", "="*30, "\n") ###########################
db_conn = None            # can use this or not, it still work in python but if u don't use this in Java it will not work
cursor = None

# I have created database "kit_b9" and now i want to create table in DB "kit_b9"
try:
    # Ask user to input DB name:
    name = input("Enter DataBase Name: ")
    # db_name = '"' + name + '"'
    db_name = name

    db_conn = psycopg2.connect(host = "localhost", port = "5432", database = db_name, user = "postgres", password = "seak1812002" )
    # db_conn.autocommit()
    db_conn.autocommit = True
    print("Connection successful.")     # if it connected it will print "connection success"
    cursor = db_conn.cursor()
    print("Cursor received")

    # Create table name: "student_mark" in SQL
    t_name = input("Name Your Table: ")   # Table name
    num = int(input("Enter Number Column you want to create: "))
    my_up = ""
    for i in range(1, num+1):
        c_name = input(f'Name for column{i}: ')
        c_type = input(f'Type for column{i}: ')
        print("===>Next===>")
        if i == num:
            my_up +=c_name +" "+c_type
        else:
            my_up +=c_name +" "+c_type+","

    print('for complete')

    # str = '"CREATE TABLE ' + t_name + str(tuple(my_up)) + ';"'

    cursor.execute("CREATE TABLE {}({});".format(t_name,my_up))
    # cursor.execute("CREATE TABLE student_mark (acc_num INTEGER, acc_name VARCHAR(50), balance INTEGER);")
    print("Table is created successfully")

except Exception as e:
    print("Issue: ", e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()              # when done all task, don't forgot to close file
    print("File is closed.")
